# Generated by Django 3.2.6 on 2022-05-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0010_studentprofile_activejobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='Web',
            field=models.TextField(null=True),
        ),
    ]