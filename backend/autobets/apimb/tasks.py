
from __future__ import absolute_import, unicode_literals
from .client import get_client
from apimb.models import Event, Runner, Market, Orders, Balance, Stakes
from matchbook.enums import Side, MarketStates, Boolean, Status
from celery import shared_task
import datetime
import logging
import json
logger = logging.getLogger(__name__)


@shared_task(bind=True)
def get_events(self):

    api = get_client()
    events = api.market_data.get_events(sport_ids=[9],states=MarketStates.All,
                                                        per_page=200, offset=0,
                                                        include_event_participants=Boolean.T,
                                                        category_ids=None, price_depth=3,
                                                        side=Side.All, session=None)
    logger.warning(f'GET EVENTS task has been called now')

    for event in events:
        event_name = event["name"]
        event_id = event['id']
        start_time = event['start']
        status = event["status"]
        sport_id = event['sport-id']
        ev, created = Event.objects.update_or_create(event_id=event_id)

        ev.event_name = event_name
        ev.sport_id = sport_id
        ev.start_time = start_time
        ev.status = status
        ev.save()

        markets = event["markets"]
        for market in markets:
            event_id = market['event-id']
            market_id = market['id']
            market_name = market['name']
            status = market['status']
            volume = market['volume']    

            ma, created = Market.objects.update_or_create(event=ev,market_id=market_id) 
            ma.market_name = market_name
            ma.status = status
            ma.volume = volume       
            ma.save()

            runners = market["runners"]
            for runner in runners:
                name = runner['name']
                runner_id = runner['id']
                try:
                    back_odds = runner['prices'][0]['odds']
                except IndexError:
                 back_odds = None
                try:
                    lay_odds = runner['prices'][3]['odds']
                except IndexError:
                 lay_odds = None            

                runner, created = Runner.objects.update_or_create(market=ma,event=ev,runner_id=runner_id)
                runner.name = name
                runner.back_odds = back_odds
                runner.lay_odds = lay_odds
                runner.save()







@shared_task(bind=True)
def get_orders(self):

    api = get_client()
    r = api.betting.get_orders(runner_ids=None, market_ids=None, offer_id=None, offset=0, per_page=500,
                   interval=None, side=Side.Default, status=Status.Open, session=None)
    logger.warning(f'GET ORDERS task has been called now')

    for d in r:
        event_name = d['event-name']
        event_id = d['event-id']
        runner_name = d['runner-name']
        created_at = d['created-at']
        id_m = d['id']
        inplay = d['in-play']
        market_id = d['market-id']
        market_name = d['market-name']
        odds = d['odds']
        remaining = d['remaining']

        pot_pro = d.get('potential-profit',0)
        rem_pot_pro =d.get('remaining-potential-profit',0)
        pot_lib = d.get('remaining-potential-liability', 0)
        runner_id = d ['runner-id']
        side = d['side']
        stake = d['stake']
        status = d['status']
        temp_id = d['temp-id']
        time_stamp = d['TIMESTAMP']


        ex, created = Orders.objects.update_or_create(temp_id=temp_id)

        ex.event_name = event_name
        ex.event_id = event_id
        ex.runner_name = runner_name
        ex.created_at = created_at
        ex.id_m = id_m
        ex.inplay = inplay
        ex.market_id = market_id
        ex.market_name = market_name
        ex.odds = odds
        ex.remaining = remaining
        ex.pot_pro = pot_pro
        ex.rem_pot_pro = rem_pot_pro
        ex.pot_lib = pot_lib
        ex.runner_id = runner_id
        ex.side = side
        ex.stake = stake
        ex.status = status
        ex.times_stamp = time_stamp
        ex.save()

    logger.info(f'Matchbook: Scraped {len(r)} from get orders')

@shared_task(bind=True)
def get_balance(self):

    api = get_client()
    r = api.account.get_account(balance_only=True)
    logger.warning(f'GET Balance task has been called now')

    balance = r.get('balance')
    exposure = r.get('exposure')
    free_funds = r.get('free-funds')
    rx, created = Balance.objects.update_or_create(balance=balance)
    rx.exposure = exposure
    rx.free_funds = free_funds
    rx.save()
    if rx.save:
        round_bal = int(float(balance))
        percent_1 = round_bal / 100 * 1
        percent_2 = round_bal / 100 * 2
        percent_3 = round_bal / 100 * 3
        percent_4 = round_bal / 100 * 4
        percent_5 = round_bal / 100 * 5
        percent_10 = round_bal /100 * 10

        ex ,created =  Stakes.objects.update_or_create(round_bal=round_bal) 
        ex.percent_1 = percent_1
        ex.percent_2 = percent_2
        ex.percent_3 = percent_3
        ex.percent_4 = percent_4
        ex.percent_5 = percent_5
        ex.percent_10 = percent_10 
        ex.save() 
        logger.info(f'Matchbook: Scraped from mb get bal')


                