# Generated by Django 3.2.6 on 2022-06-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0013_auto_20220601_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='Resume',
            field=models.FileField(default='', null=True, upload_to='WEBAPP/files'),
        ),
    ]