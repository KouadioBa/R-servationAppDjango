from django.db import models

class Classes(models.Model):
    entite = models.CharField(max_length=200)
    classe = models.CharField(max_length=200)
    motif = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    heure = models.CharField(max_length=200)
    intervenant = models.TextField(max_length=200)
    matiere = models.TextField(max_length=200)
    salle = models.CharField(max_length=200)

    def __str__(self):
        return self.entite