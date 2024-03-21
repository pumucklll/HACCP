# Generated by Django 5.0.3 on 2024-03-21 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Benutzer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benutzer_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Checkliste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkliste_name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='MangelArt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mangelart_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ObjektOrt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objektort_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='oknok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oknok_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Audit_Ereignis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist', models.DateField()),
                ('behoben', models.DateTimeField()),
                ('pruefpunkt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccp.audit')),
                ('von', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccp.benutzer')),
                ('checkliste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccp.checkliste')),
                ('mangel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccp.mangelart')),
                ('objektort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccp.objektort')),
                ('ok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haccp.oknok')),
            ],
        ),
    ]
