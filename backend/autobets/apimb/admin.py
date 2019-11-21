
from django.contrib import admin
from apimb.models import Event, Runner,Market, Balance, Orders, Stakes, Bet, BetTriggers, EventMonitor, UserStakes


class EventAdmin(admin.ModelAdmin):

    list_display = ('sport_id', 'event_id', 'event_name', 'start_time','status')
    search_fields = ('event_name','event_id')
    ordering = ['start_time']

admin.site.register(Event, EventAdmin)

class MarketAdmin(admin.ModelAdmin):

    list_display = ('market_id', 'market_name', 'status', 'volume')
    search_fields = ('market_name','status')
    ordering = ['volume']

admin.site.register(Market, MarketAdmin)

class RunnerAdmin(admin.ModelAdmin):

    list_display = ('name', 'runner_id', 'back_odds', 'lay_odds')
    search_fields = ('name','runner_id')

admin.site.register(Runner, RunnerAdmin)


class BalanceAdmin(admin.ModelAdmin):

    list_display = ('balance','exposure','free_funds')

admin.site.register(Balance, BalanceAdmin)

class OrdersAdmin(admin.ModelAdmin):

    list_display = ('event_name', 'runner_name', 'side', 'stake', 
                    'time_stamp', 'created_at','odds','remaining' ,
                    'status' ,'inplay')
    
    search_fields = ('runner_name',)
    ordering = ['created_at']

admin.site.register(Orders, OrdersAdmin)

class StakesAdmin(admin.ModelAdmin):

    list_display = ('round_bal','percent_1','percent_2',
                    'percent_3','percent_4','percent_5',
                    'percent_10')

admin.site.register(Stakes, StakesAdmin)

class EventMonitorAdmin(admin.ModelAdmin):

    list_display = ('event_id','event_name','status',
                    'is_ip')

admin.site.register(EventMonitor, EventMonitorAdmin)



class BetAdmin(admin.ModelAdmin):


    list_display = ('runner_name','runner_id','price','side',
                    'status','size_remaining','size_matched',
                    'price','back','lay')

admin.site.register(Bet, BetAdmin)

class BetTriggersAdmin(admin.ModelAdmin):


    list_display = ('b1_trig','b2_trig','l1_trig',
                    'l2_trig','runner_name','runner_id',
                    )

admin.site.register(BetTriggers, BetTriggersAdmin)

class UserStakesAdmin(admin.ModelAdmin):


    list_display = ('back_stake','lay_stake')

admin.site.register(UserStakes, UserStakesAdmin)