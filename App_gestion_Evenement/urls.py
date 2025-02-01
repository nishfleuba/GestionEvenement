from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('evenement', views.EvenementViewSet)
router.register('ticket', views.TicketViewSet)
router.register('participant', views.ParticipantViewSet)




urlpatterns = [
    path('', include(router.urls)),
    path('api_auth', include('rest_framework.urls')),
]