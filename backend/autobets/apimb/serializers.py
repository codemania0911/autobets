from rest_framework import serializers
from .models import Event, Market, Runner, Balance

class EventSerializer(serializers.ModelSerializer):

    start_time = serializers.DateTimeField(read_only=True, format="%d-%m-%y")
    class Meta:
        model = Event
        fields =['id','sport_id','event_name','start_time','status','event_id']

class MarketSerializer(serializers.ModelSerializer):


    class Meta:
        model = Market
        fields =['id','market_id','market_name','status','volume','event']       

class RunnerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Runner
        fields ='__all__' 

class CombinedSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    market = MarketSerializer()

    class Meta:
        model = Runner
        fields = ('id','url' 'name', 'event' ,'market')
    


class BalanceSerializer(serializers.ModelSerializer):


    class Meta:
        model = Balance
        fields =['id','balance','exposure','free_funds']         
        