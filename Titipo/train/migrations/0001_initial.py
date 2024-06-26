# Generated by Django 5.0.3 on 2024-04-04 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('trainID', models.AutoField(primary_key=True, serialize=False)),
                ('depart', models.CharField(max_length=50)),
                ('arrivee', models.CharField(max_length=50)),
                ('heureDepart', models.CharField(max_length=6)),
                ('heureArrivee', models.CharField(max_length=6)),
                ('dureeTrajet', models.CharField(max_length=6)),
                ('info', models.CharField(max_length=4000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/IMG/')),
                ('prix', models.CharField(max_length=10)),
            ],
        ),
    ]

