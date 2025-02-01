from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class EvenementSerializer(serializers.ModelSerializer):
    organisateur=serializers.StringRelatedField()
    class Meta:
        model=Evenement
        fields=('nom','description','date','location','organisateur')


    def to_representation(self, instance):
        representation = super().to_representation(instance)  
        representation['organisateur'] = str(instance.organisateur)  
        return representation 

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=( 'evenement','acheteur','prix','date_achat' )
    def to_representation(self, instance):
        representation = super().to_representation(instance)  
        representation['evenement']=EvenementSerializer(instance.evenement).data
        representation['acheteur'] = str(instance.acheteur)
 
        return representation

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model=Participant
        fields=('evenement','participant')
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['evenement']=EvenementSerializer(instance.evenement).data  
        representation['participant']=str(instance.participant)
        return representation  