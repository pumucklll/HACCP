from django.db import models
from django.forms import DateTimeField
from django.utils import timezone


class check(models.TextChoices):
    A = "1", "VERKAUFSRAUM / GASTRAUM"
    B = "2", "Be- und Verarbeitungsraum / Küche"
    C = "3", "Kühlraum / Tiefkühlraum"
    D = "4", "Lagerraum."
    E = "5", "Personal-, Sanitär- und sonstige Nebenräume"


class objekt_ort(models.Model):
    eintrag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.eintrag}"


class pruef(models.Model):
    pruefung = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.pruefung}"


class oknok(models.TextChoices):
    ok = "1", "in Ordnung"
    nok = "2", "nicht in Ordnung"


class mangel_art(models.Model):
    mangel = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.mangel}"


class ToDoItem(models.Model):
    checkliste = models.CharField(max_length=3, choices=check.choices, default=check.A)
    objektort = models.ForeignKey(objekt_ort, on_delete=models.CASCADE)
    pruefpunkt = models.ForeignKey(pruef, on_delete=models.CASCADE)
    ok = models.CharField(max_length=3, choices=oknok.choices, default=oknok.ok)
    mangel = models.ForeignKey(mangel_art, on_delete=models.CASCADE)
    frist = models.CharField(max_length=100, default="frist")
    behoben = models.DateTimeField()
    von = models.CharField(max_length=100, default="von")

    def __str__(self):
        return (f"{self.checkliste}: {self.objektort} : {self.pruefpunkt}  : {self.ok} "
                f": {self.mangel} : {self.frist} : {self.behoben}: {self.von} ")
