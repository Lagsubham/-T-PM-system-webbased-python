from cgi import print_exception
from email.policy import default
from django.db import models
from numpy import product
import datetime
from django.utils import timezone, dateformat


# Create your models here.


class StudentProfile(models.Model):
    id = models.AutoField
    StudentId  = models.CharField(max_length=50, default="")
    StudentDob = models.DateField(null=True)
    Department=models.CharField(max_length=50,default="")
    Semester=models.IntegerField(default=0)
    AverageMarks= models.IntegerField(default=0)
    AddmissionY = models.DateField(null=True)
    FsemM = models.IntegerField(default=0)
    FsemMS = models.FileField(upload_to="WEBAPP/files", default="")
    SsemM = models.IntegerField(default=0)
    SsemMS = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    TsemM = models.IntegerField(default=0)
    TsemMS = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    FosemM = models.IntegerField(default=0)
    FosemMS = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    FisemM = models.IntegerField(default=0)
    FisemMS = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    SisemM = models.IntegerField(default=0)
    SisemMS = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    SesemM = models.IntegerField(default=0)
    SesemMS = models.FileField(upload_to="WEBAPP/files", default="" ,null=True)
    EosemM = models.IntegerField(default=0)
    EosemMS = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    Resume = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    JobsAchiv = models.IntegerField(default=0)
    Stdimage = models.ImageField(upload_to="WEBAPP/images", default="")
    Appld_job = models.IntegerField(default=0)
    FromFilld = models.IntegerField(default=0)
    activeJobs = models.TextField(null=True)
    Appld_Train = models.IntegerField(default=0)
    activeTrains = models.TextField(null=True)
    StatusJ = models.TextField(null=True)
    AppDtJ = models.TextField(null=True)
    StatusT = models.TextField(null=True)
    AppDtT = models.TextField(null=True)

    def __str__(self):
        return self.StudentId

class Company(models.Model):
    id =  models.AutoField
    CompanyId = models.CharField(max_length=50, default="")
    CompanyNm = models.CharField(max_length=50,default="")
    Cmnyimage = models.ImageField(upload_to="FASHION/images", default="", null=True)
    ComPort = models.FileField(upload_to="WEBAPP/files", default="", null=True)
    ComAdd = models.CharField(max_length=50,default="")
    FromFilld = models.IntegerField(default=0)
    Web = models.TextField(null=True)
    def __str__(self):
        return self.CompanyId

class Job(models.Model):
    Jid = models.AutoField
    jobTitle = models.CharField(max_length=50,default="")
    jobDesc = models.CharField(max_length=250,default="")
    JobCrit = models.IntegerField(default=0)
    JobMarks = models.IntegerField(default=0)
    JObDept = models.CharField(max_length=50,default="")
    Company = models.CharField(max_length=50,default="")
    JobAppl = models.IntegerField(default=0)
    ApplList = models.TextField(null=True)
    def __str__(self):
        return self.jobTitle


class Training(models.Model):
    Tid = models.AutoField
    TrainTitle = models.CharField(max_length=50,default="")
    TrainDesc = models.CharField(max_length=250,default="")
    TrainCrit = models.IntegerField(default=0)
    TrainMarks = models.IntegerField(default=0)
    TrainDept = models.CharField(max_length=50,default="")
    Company = models.CharField(max_length=50,default="")
    TrainAppl = models.IntegerField(default=0)
    ApplList = models.TextField(null=True)
    def __str__(self):
        return self.TrainTitle