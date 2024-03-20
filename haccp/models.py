from django.db import models
from django.forms import DateTimeField
from django.utils import timezone


class Checkliste(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name}"


class ObjektOrt(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Audit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"



class oknok(models.Model):
    name = models.CharField(max_length=50,)

    def __str__(self):
        return f"{self.name}"



#class oknok(models.TextChoices):
#    ok = "1", "in Ordnung"
#    nok = "2", "nicht in Ordnung"



class MangelArt(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Benutzer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Audit_Ereignis(models.Model):
    checkliste = models.ForeignKey(Checkliste, on_delete=models.CASCADE)
    objektort = models.ForeignKey(ObjektOrt, on_delete=models.CASCADE)
    pruefpunkt = models.ForeignKey(Audit, on_delete=models.CASCADE)
    ok = models.ForeignKey(oknok, on_delete=models.CASCADE)
    mangel = models.ForeignKey(MangelArt, on_delete=models.CASCADE,)
    frist = models.DateField()
    behoben = models.DateTimeField()
    von = models.ForeignKey(Benutzer, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.checkliste}: {self.objektort} : {self.pruefpunkt}  : {self.ok} "
                f": {self.mangel} : {self.frist} : {self.behoben}: {self.von} ")
