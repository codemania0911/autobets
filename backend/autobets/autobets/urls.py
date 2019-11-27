from django.contrib import admin
from django.urls import path, include

from rest_framework import routers


from apimb.views import (EventViewSet, MarketViewSet, RunnerViewSet, BalanceViewSet, CombinedViewSet,
                         PandLViewSet)

router = routers.DefaultRouter()
router.register('events', EventViewSet)
router.register('markets', MarketViewSet)
router.register('runners', RunnerViewSet)
router.register('balance', BalanceViewSet)
router.register('combined', CombinedViewSet, base_name='combined1')
router.register('reports', PandLViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]
