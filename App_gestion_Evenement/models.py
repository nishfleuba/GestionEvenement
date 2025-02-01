from django.db import models
from django.contrib.auth.models import User  

class Evenement(models.Model):
    nom = models.CharField(max_length=255)  
    description = models.TextField()  
    date = models.DateTimeField()  
    location = models.CharField(max_length=255)  
    organisateur = models.ForeignKey(User, on_delete=models.CASCADE)   

    def __str__(self):
        return self.nom


class Ticket(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)  
    acheteur = models.ForeignKey(User, on_delete=models.CASCADE)  
    prix = models.DecimalField(max_digits=10, decimal_places=2)  
    date_achat = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Ticket pour {self.evenement.nom} - Acheteur: {self.acheteur.username}"


class Participant(models.Model):
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)  
    participant = models.ForeignKey(User, on_delete=models.CASCADE)  
 

    def __str__(self):
        return f"{self.participant.username} participe à {self.evenement.nom}"
