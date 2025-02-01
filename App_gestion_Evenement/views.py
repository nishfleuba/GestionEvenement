from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

class EvenementViewSet(viewsets.ModelViewSet):
    queryset=Evenement.objects.all()
    serializer_class=EvenementSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset=Ticket.objects.all()
    serializer_class=TicketSerializer

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset=Participant.objects.all()
    serializer_class=ParticipantSerializer
