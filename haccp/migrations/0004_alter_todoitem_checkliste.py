# Generated by Django 5.0.3 on 2024-03-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haccp', '0003_todoitem_behoben'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='checkliste',
            field=models.CharField(choices=[('1', 'VERKAUFSRAUM / GASTRAUM'), ('2', 'Be- und Verarbeitungsraum / Küche'), ('3', 'Kühlraum / Tiefkühlraum'), ('4', 'Lagerraum.'), ('5', 'Personal-, Sanitär- und sonstige Nebenräume')], default='1', max_length=3),
        ),
    ]
