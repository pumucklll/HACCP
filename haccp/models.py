from django.db import models
from django.forms import DateTimeField
from django.utils import timezone


class Checkliste(models.Model):
    liste = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.liste}"


class ObjektOrt(models.Model):
    eintrag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.eintrag}"


class Audit(models.Model):
    pruefung = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pruefung}"


class oknok(models.TextChoices):
    ok = "1", "in Ordnung"
    nok = "2", "nicht in Ordnung"


class MangelArt(models.Model):
    mangel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mangel}"


class Benutzer(models.Model):
    benutzer = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.benutzer}"


class Audit_Ereignis(models.Model):
    checkliste = models.ForeignKey(Checkliste, on_delete=models.CASCADE)
    objektort = models.ForeignKey(ObjektOrt, on_delete=models.CASCADE)
    pruefpunkt = models.ForeignKey(Audit, on_delete=models.CASCADE)
    ok = models.CharField(max_length=3, choices=oknok.choices, default=oknok.ok)
    mangel = models.ForeignKey(MangelArt, on_delete=models.CASCADE, blank=True,null=True)
    frist = models.DateField(blank=True,null=True)
    behoben = models.DateTimeField()
    von = models.ForeignKey(Benutzer, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.checkliste}: {self.objektort} : {self.pruefpunkt}  : {self.ok} "
                f": {self.mangel} : {self.frist} : {self.behoben}: {self.von} ")
