# Generated by Django 5.0.3 on 2024-03-18 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haccp', '0012_alter_checkliste_liste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audit_ereignis',
            name='mangel',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='haccp.mangelart'),
        ),
    ]
