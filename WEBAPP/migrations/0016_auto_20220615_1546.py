# Generated by Django 3.2.6 on 2022-06-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0015_auto_20220615_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentprofile',
            old_name='AppDt',
            new_name='AppDtJ',
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='AppDtT',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='StatusT',
            field=models.TextField(null=True),
        ),
    ]
