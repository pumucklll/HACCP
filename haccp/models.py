from django.db import models
from django.forms import DateTimeField
from django.utils import timezone


class Checkliste(models.Model):
    checkliste_name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return f"{self.checkliste_name}"


class ObjektOrt(models.Model):
    objektort_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.objektort_name}"


class Audit(models.Model):
    audit_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.audit_name}"



class oknok(models.Model):
    oknok_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.oknok_name}"




class MangelArt(models.Model):
    mangelart_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.mangelart_name}"


class Benutzer(models.Model):
    benutzer_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.benutzer_name}"


class Audit_Ereignis(models.Model):
    checkliste = models.ForeignKey(Checkliste, on_delete=models.CASCADE, to_field='checkliste_name', default='Checkliste A')
    objektort = models.ForeignKey(ObjektOrt, on_delete=models.CASCADE, to_field='objektort_name', default='Boden')
    pruefpunkt = models.ForeignKey(Audit, on_delete=models.CASCADE, to_field='audit_name', default='sauber')
    ok = models.ForeignKey(oknok, on_delete=models.CASCADE, to_field='oknok_name', default='in Ordnung')
    mangel = models.ForeignKey(MangelArt, on_delete=models.CASCADE, to_field='mangelart_name', default='keiner')
    frist = models.DateField()
    behoben = models.DateTimeField()
    von = models.ForeignKey(Benutzer, on_delete=models.CASCADE, to_field='benutzer_name', default='Gerhard')

    def __str__(self):
        return (f"{self.checkliste}: {self.objektort} : {self.pruefpunkt}  : {self.ok} "
                f": {self.mangel} : {self.frist} : {self.behoben}: {self.von} ")
