# Generated by Django 5.0.3 on 2024-03-18 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haccp', '0011_benutzer_checkliste_alter_audit_ereignis_frist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkliste',
            name='liste',
            field=models.CharField(max_length=80),
        ),
    ]
