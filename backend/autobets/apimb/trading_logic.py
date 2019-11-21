from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from .client import get_client
from .models import Stakes, UserStakes, BetTriggers
from matchbook.enums import Side
from matchbook.endpoints.betting import Betting
from matchbook.enums import Side, Status, AggregationType



@receiver(post_save, sender=BetTriggers)
def check_bet_triggers(sender, instance, created, **kwargs):


    get_user_stake = UserStakes.objects.get(id=1)
    user_back_order = get_user_stake.back_stake
    user_lay_order = get_user_stake.lay_stake

    pass



'''
1  If instance is Autostake use Autostake
2  If instance is User Stake use UserStake
3  If Trigger is met place Bet
4
5
6
'''


