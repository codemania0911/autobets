from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(null=True, max_length=30)
    password = models.CharField(null=True, max_length=30)

class SessionToken(models.Model):
    session_token = models.CharField(null=True, max_length=40)

class Balance(models.Model):
    exposure = models.FloatField(null=True)
    balance = models.FloatField(null=True)
    free_funds = models.FloatField(null=True)
    round_bal= models.IntegerField(null=True)
    percent_1 = models.FloatField(null=True)
    percent_2 = models.FloatField(null=True)
    percent_3 = models.FloatField(null=True)
    percent_4 = models.FloatField(null=True)
    percent_5 = models.FloatField(null=True)
    percent_6 = models.FloatField(null=True)
    percent_7 = models.FloatField(null=True)
    percent_8 = models.FloatField(null=True)
    percent_9 = models.FloatField(null=True)
    percent_10 = models.FloatField(null=True)


class Orders(models.Model):
    market_id = models.BigIntegerField(null=True)
    temp_id = models.CharField(null=True,max_length=20)
    event_name = models.CharField(max_length=200, null=True)
    time_stamp = models.DateTimeField(null=True)
    event_id = models.BigIntegerField(null=True)
    market_name = models.CharField(max_length=12, null=True)
    market_type = models.CharField(max_length=13, null=True)
    runner_id = models.BigIntegerField(null=True)
    runner_name = models.CharField(max_length=100, null=True)
    side = models.CharField(max_length=9, null=True)
    odds = models.FloatField(null=True)
    odds_type = models.CharField(max_length=20,null=True)
    stake = models.IntegerField(null=True)
    remaining = models.IntegerField(null=True)
    pot_pro = models.IntegerField(null=True)
    rem_pot_pro = models.IntegerField(null=True)
    pot_lib = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=40, null=True)
    inplay = models.CharField(max_length=20,null=True)

class Stakes(models.Model):
    round_bal = models.FloatField(null=True)
    percent_1 = models.FloatField(null=True)
    percent_2 = models.FloatField(null=True)
    percent_3 = models.FloatField(null=True)
    percent_4 = models.FloatField(null=True)
    percent_5 = models.FloatField(null=True)
    percent_10 = models.FloatField(null=True)

class UserStakes(models.Model):
    back_stake = models.IntegerField(blank=True)
    lay_stake = models.IntegerField(blank=True)    


class Book(models.Model):
    status = models.CharField(max_length=50)
    bet_delay = models.FloatField(null=True)
    inplay = models.BooleanField()
    number_of_winners = models.IntegerField(null=True)
    number_of_runners = models.IntegerField(null=True)
    total_matched = models.FloatField(null=True)

class RunnerBook(models.Model):
    status = models.CharField(max_length=20)
    last_price_traded = models.FloatField(null=True)
    total_matched = models.FloatField(null=True)
    back_price = models.FloatField(null=True)
    back_size = models.FloatField(null=True)
    lay_price = models.FloatField(null=True)
    lay_size = models.FloatField(null=True)

class BetTriggers(models.Model):
    
    b1_trig = models.CharField(max_length=30, null=True)
    b2_trig = models.CharField(max_length=30, null=True)
    l1_trig = models.CharField(max_length=30, null=True)
    l2_trig = models.CharField(max_length=30, null=True)
    runner_name = models.CharField(max_length=300)
    runner_id = models.BigIntegerField(null=True)

class Bet(models.Model):

    bet_id = models.BigIntegerField(null=True)
    runner_name = models.CharField(max_length=300,null=True)
    runner_id = models.BigIntegerField(null=True)
   # est = models.FloatField()
    trade = models.FloatField(null=True)
    back = models.FloatField(null=True)
    lay = models.FloatField(null=True)
    margin = models.FloatField(null=True)
    bracket = models.IntegerField(null=True)
    payout = models.FloatField(null=True)
    liability = models.FloatField(null=True)

    order_type = models.CharField(max_length=50)
    persistence_type = models.CharField(max_length=50)
    placed_at = models.DateTimeField()
    price = models.FloatField(null=True)
    size = models.FloatField(null=True)
    side = models.CharField(max_length=20)
    size_matched = models.FloatField(null=True)
    size_remaining = models.FloatField(null=True)
    size_lapsed = models.FloatField(null=True)
    size_cancelled = models.FloatField(null=True)
    size_voided = models.FloatField(null=True)
    status = models.CharField(max_length=30)

    outcome = models.CharField(max_length=50, null=True)
    profit = models.FloatField(null=True)  

class EventMonitor(models.Model):
    sport = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    live = models.CharField(max_length=50, null=True)
    stage = models.CharField(max_length=50, null=True)
    event_id = models.BigIntegerField(primary_key=True)
    event_name = models.CharField(max_length=200, null=True)
    start_time = models.DateTimeField(null=True)
    open_date = models.CharField(null=True, max_length=50)
    cat_name = models.CharField(null=True,max_length=50)
    market_type = models.CharField(null=True,max_length=50)
    status = models.CharField(null=True,max_length=13)
    is_ip = models.CharField(null=True, max_length=10)
    competition = models.CharField(null=True, max_length=50)


class Event(models.Model):
    sport_id = models.CharField(max_length=15)
    event_id = models.BigIntegerField(unique=True)
    event_name = models.CharField(max_length=200)
    start_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=13)
    

class Market(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    market_id = models.BigIntegerField(unique=True)
    market_name = models.CharField(max_length=35)
    status = models.CharField(max_length=10)
    volume = models.FloatField(null=True)
    is_ip = models.CharField(max_length=5)

class Runner(models.Model):
    event = models.ForeignKey(Event, null=True, default=None, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, null=True, default=None, on_delete=models.CASCADE)
    runner_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=500)
    back_odds = models.FloatField(null=True)
    lay_odds = models.FloatField(null=True)


class ReportsMarket(models.Model):

    i_d = models.CharField(null=True, max_length=50)
    name = models.CharField(null=True, max_length=50)
    event_id = models.CharField(null=True, max_length=50)
    event_name = models.CharField(null=True, max_length=50)
    sport_id = models.CharField(null=True, max_length=50)
    start_time = models.CharField(null=True, max_length=50)
    settled_time = models.CharField(null=True, max_length=50)
    stake = models.CharField(null=True, max_length=50)
    profit_and_loss = models.CharField(null=True, max_length=50)
    commission = models.CharField(null=True, max_length=50)
    profit_and_loss = models.CharField(null=True, max_length=50)
    net_profit_and_loss = models.CharField(null=True, max_length=50)
    selections = models.CharField(null=True, max_length=50)

class ReportsSelections(models.Model):
    runner_id = models.CharField(null=True, max_length=50)
    runner_name = models.CharField(null=True, max_length=50)
    side = models.CharField(null=True, max_length=50)
    odds = models.CharField(null=True, max_length=50)
    stake = models.CharField(null=True, max_length=50)
    profit_and_loss = models.CharField(null=True, max_length=50)
    commission = models.CharField(null=True, max_length=50)
    net_profit_and_loss = models.CharField(null=True, max_length=50)
    bets = models.CharField(null=True, max_length=50)       

class ReportsBets(models.Model):
    i_d = models.CharField(null=True, max_length=50) 
    offer_id = models.CharField(null=True, max_length=50) 
    odds = models.CharField(null=True, max_length=50) 
    stake = models.CharField(null=True, max_length=50) 
    adjusted = models.CharField(null=True, max_length=50) 
    originator = models.CharField(null=True, max_length=50) 
    inplay = models.CharField(null=True, max_length=50) 
    submitted_time = models.CharField(null=True, max_length=50) 
    matched_time = models.CharField(null=True, max_length=50) 
    settled_time = models.CharField(null=True, max_length=50) 
    result = models.CharField(null=True, max_length=50) 
    profit_and_loss = models.CharField(null=True, max_length=50) 
    commission_type = models.CharField(null=True, max_length=50) 
    net_profit_and_loss = models.CharField(null=True, max_length=50) 