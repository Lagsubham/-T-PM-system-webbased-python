# Generated by Django 3.2.6 on 2022-05-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='FromFilld',
            field=models.IntegerField(default=0),
        ),
    ]
