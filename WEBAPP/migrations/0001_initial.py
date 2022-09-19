# Generated by Django 3.2.6 on 2022-05-30 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_ID', models.CharField(default='', max_length=50)),
                ('CompanyNm', models.CharField(default='', max_length=50)),
                ('Cmnyimage', models.ImageField(default='', upload_to='FASHION/images')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(default='', max_length=50)),
                ('jobDesc', models.CharField(default='', max_length=250)),
                ('JobCrit', models.CharField(default='', max_length=50)),
                ('JobMarks', models.IntegerField(default=0)),
                ('JObDept', models.CharField(default='', max_length=50)),
                ('Company', models.CharField(default='', max_length=50)),
                ('JobAppl', models.IntegerField(default=0)),
                ('ApplList', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StudentId', models.CharField(default='', max_length=50)),
                ('StudentDob', models.DateField()),
                ('Department', models.CharField(default='', max_length=50)),
                ('Semester', models.CharField(default='', max_length=50)),
                ('AverageMarks', models.IntegerField(default=0)),
                ('AddmissionY', models.DateField()),
                ('FsemM', models.IntegerField(default=0)),
                ('FsemMS', models.FileField(default='', upload_to='FASHION/files')),
                ('SsemM', models.IntegerField(default=0)),
                ('SsemMS', models.FileField(default='', upload_to='FASHION/files')),
                ('TsemM', models.IntegerField(default=0)),
                ('TsemMS', models.FileField(default='', upload_to='FASHION/files')),
                ('FosemM', models.IntegerField(default=0)),
                ('FosemMS', models.FileField(default='', upload_to='FASHION/files')),
                ('JobsAchiv', models.IntegerField(default=0)),
                ('Stdimage', models.ImageField(default='', upload_to='FASHION/images')),
                ('Appld_job', models.IntegerField(default=0)),
            ],
        ),
    ]