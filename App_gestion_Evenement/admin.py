from django.contrib import admin
from .models import *

@admin.register(Evenement)
class EventAdmin(admin.ModelAdmin):
    list_display=('nom','description','date','location','organisateur')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=('evenement','acheteur','prix','date_achat')

@admin.register(Participant)
class TicketAdmin(admin.ModelAdmin):
    list_display=('evenement','participant')