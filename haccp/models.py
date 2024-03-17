from django.db import models
from django.forms import DateTimeField
from django.utils import timezone


class ToDoItem(models.Model):
    checkliste = models.CharField(max_length=100, default="checkliste")
    objekt = models.CharField(max_length=100, default="objekt")
    pruefpunkt = models.CharField(max_length=100, default="pruefpunkt")
    ok = models.CharField(max_length=100, default="ok")
    mangel = models.CharField(max_length=100, default="mangel")
    frist = models.CharField(max_length=100, default="frist")
    behoben = models.DateTimeField()
    von = models.CharField(max_length=100, default="von")

    def __str__(self):
        return (f"{self.checkliste}: {self.objekt} : {self.pruefpunkt}  : {self.ok} "
                f": {self.mangel} : {self.frist} : {self.behoben}: {self.von} ")
