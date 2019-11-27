from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import mixins, viewsets, permissions, status
from rest_framework.views import APIView

from celery.signals import after_task_publish
from .models import Event, Market, Runner, Balance, ReportsMarket
from .tasks import get_events
from .serializers import (
                        EventSerializer, MarketSerializer, RunnerSerializer, BalanceSerializer, 
                        CombinedSerializer, ProfitAndLossSerializer)
from .permissions import EventPermission


class EventViewSet(mixins.ListModelMixin, 
                   mixins.DestroyModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    queryset = Event.objects.all().order_by('start_time')
    serializer_class = EventSerializer
    permission_classes = (EventPermission, )
    
    #get_events.delay()


class MarketViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet,
                    mixins.RetrieveModelMixin):
                    
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

class RunnerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Runner.objects.all()
    serializer_class = RunnerSerializer   

class BalanceViewSet(mixins.ListModelMixin, 
                    viewsets.GenericViewSet, 
                    mixins.RetrieveModelMixin):

    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer 

class CombinedViewSet(mixins.ListModelMixin, 
                    viewsets.GenericViewSet, 
                    mixins.RetrieveModelMixin):


    queryset = Runner.objects.all()
    serializer_class = CombinedSerializer     
    
class PandLViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):

    queryset = ReportsMarket.objects.all().order_by('start_time')
    serializer_class = ProfitAndLossSerializer