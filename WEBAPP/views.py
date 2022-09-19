from django.shortcuts import render,  HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
import joblib
from .models import Job, Company, StudentProfile, Training
import json
from datetime import date
# from math import ceil
# Create your views here.

def is_member(user,group_name):
    return user.groups.filter(name=group_name).exists()


def json_2_list(json_S):
    json_S = "[" + json_S + "]"
    return json.loads(json_S)


def list_2_json(list_var):
    list_var = json.dumps(list_var)
    return list_var[1:-1]

def home(request):
    return render(request, "WEBAPP/login.html")

@login_required   
def logout_site(request):
    logout(request)
    return render(request, "WEBAPP/login.html")
 

def login_site(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            
           
            if is_member(user,"Company") == True :
                fromfilld = Company.objects.filter(CompanyId = username)
                login_mssge= "Login Successfully"
                home_mssge = [request.user,1]
                login(request, user)
                if fromfilld[0].FromFilld == 0:
                    return render(request, "WEBAPP/ComForm.html")
                else:
                    return redirect(CompanyDash)
                # home(request)
                # return render(request, "FASHION/home.html",  {'login_mssge': login_mssge , 'home_mssge':home_mssge[1],'user':home_mssge[0]})
            if is_member(user,"Students") == True:
                fromfilld = StudentProfile.objects.filter(StudentId = username)
                login_mssge= "Login Successfully"
                home_mssge = [request.user,1]
                login(request, user)
                if fromfilld[0].FromFilld == 0:
                    return render(request, "WEBAPP/SemSel.html")
                else:
                    return redirect(StudentDash)
                # return redirect(DASH)
                # return render(request, "FASHION/DASH.html",  {'login_mssge': login_mssge , 'home_mssge':home_mssge[1],'user':home_mssge[0]})
        else:
            login_mssge= ["No user found", 2]
            return render(request, "WEBAPP/login.html" , {'login_mssge': login_mssge})
    else:
        return render(request, "WEBAPP/login.html")

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        group = request.POST['group']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2 and User.objects.filter(username=username).exists()== False:
            newUser = User.objects.create_user(username, email, password1)
            if group == "Company":
                newUserData = Company(CompanyId=username)
                newUserData.save()
            else:
                newUserData = StudentProfile(StudentId=username)
                newUserData.save()
            newUser.first_name = fname
            newUser.last_name = lname
            my_group = Group.objects.get(name=group)
            my_group.user_set.add(newUser)
            newUser.save()
            login_mssge = "Successfully created your account please Login"
            return render(request, "WEBAPP/login.html", {'login_mssge': login_mssge})
        elif password1!= password2:
            messages_signup = ["Password does not matched with Confirm password",1]
            return render(request, "WEBAPP/signup.html", {'messages_signup': messages_signup})
        elif User.objects.filter(username=username).exists():
            messages_signup =["Please check anothe user name",1]
            return render(request, "WEBAPP/signup.html", {'messages_signup': messages_signup})
        elif password1 != password2 and User.objects.filter(username=username).exists():
            messages_signup = ["Please check anothe user name and Password does not matched with Confirm password",1]
            return render(request, "WEBAPP/signup.html", {'messages_signup': messages_signup})
        else:
            return render(request, "404.html")
    else:
        return render(request, "WEBAPP/signup.html")


#############################################################################################################
######################################## STUDENT AREA ######################################################
###########################################################################################################

 
@login_required
def SemSel(request):
    if request.method == 'POST':
        StudentId = StudentProfile.objects.filter(StudentId = request.user) 
        user = StudentId[0]
        user.Semester = request.POST['Semester']
        user.Department = request.POST['Department']
        user.StudentDob = request.POST['StudentDob']
        user.AverageMarks = request.POST['AverageMarks']
        user.AddmissionY = request.POST['AddmissionY']
        user.save()
        Sem =  {'sem' : range(1,int(request.POST['Semester']))}
    return render(request, "WEBAPP/FromFillup.html", Sem)


@login_required
def FromFillup(request):
    if request.method == 'POST':
        StudentId = request.user
        User = StudentProfile.objects.filter(StudentId = StudentId)
        User = User[0]
        
        User.FsemM = request.POST['semM1']
        User.FsemMS = request.FILES['semMS1']
        Sem = int(User.Semester)-1
        if Sem == 2 :
            User.SsemM = request.POST['semM2']
            User.SsemMS = request.FILES['semMS2']
        elif Sem == 3:
            User.SsemM = request.POST['semM2']
            User.SsemMS = request.FILES['semMS2']
            User.TsemM = request.POST['semM3']
            User.TsemMS = request.FILES['semMS3']
        elif Sem == 4 :
            User.SsemM = request.POST['semM2']
            User.SsemMS = request.FILES['semMS2']
            User.TsemM = request.POST['semM3']
            User.TsemMS = request.FILES['semMS3']
            User.FosemM = request.POST['semM4']
            User.FosemMS = request.FILES['semMS4']
        elif Sem == 5:
            User.SsemM = request.POST['semM2']
            User.SsemMS = request.FILES['semMS2']
            User.TsemM = request.POST['semM3']
            User.TsemMS = request.FILES['semMS3']
            User.FosemM = request.POST['semM4']
            User.FosemMS = request.FILES['semMS4']
            User.FisemM = request.POST['semM5']
            User.FisemMS = request.FILES['semMS5']
        elif Sem == 6 :
            User.SsemM = request.POST['semM2']
            User.SsemMS = request.FILES['semMS2']
            User.TsemM = request.POST['semM3']
            User.TsemMS = request.FILES['semMS3']
            User.FosemM = request.POST['semM4']
            User.FosemMS = request.FILES['semMS4']
            User.FisemM = request.POST['semM5']
            User.FisemMS = request.FILES['semMS5']
            User.SisemM = request.POST['semM6']
            User.SisemMS = request.FILES['semMS6']
        elif Sem == 7:
            User.SsemM = request.POST['semM2']
            User.SsemMS = request.FILES['semMS2']
            User.TsemM = request.POST['semM3']
            User.TsemMS = request.FILES['semMS3']
            User.FosemM = request.POST['semM4']
            User.FosemMS = request.FILES['semMS4']
            User.FisemM = request.POST['semM5']
            User.FisemMS = request.FILES['semMS5']
            User.SisemM = request.POST['semM6']
            User.SisemMS = request.FILES['semMS6']
            User.SesemM = request.POST['semM7']
            User.SesemMS = request.FILES['semMS7']
        elif Sem == 8:
            User.SsemM = request.POST['semM2']
            User.SsemMS = request.FILES['semMS2']
            User.TsemM = request.POST['semM3']
            User.TsemMS = request.FILES['semMS3']
            User.FosemM = request.POST['semM4']
            User.FosemMS = request.FILES['semMS4']
            User.FisemM = request.POST['semM5']
            User.FisemMS = request.FILES['semMS5']
            User.SisemM = request.POST['semM6']
            User.SisemMS = request.FILES['semMS6']
            User.SesemM = request.POST['semM7']
            User.SesemMS = request.FILES['semMS7']
            User.EsemM = request.POST['semM8']
            User.EsemMS = request.FILES['semMS8']
        User.Stdimage = request.FILES['Stdimage']
        User.FromFilld = 1
        User.save()
        return redirect(StudentDash)







@login_required
def StudentDash(request):
    currentUser = request.user
    Userdata = StudentProfile.objects.filter(StudentId = currentUser)
    Userdata = Userdata[0]
    dept = Userdata.Department
    if Userdata.Semester == 0:
        cri = 0
    else:
        cri = int(Userdata.Semester) -1
        # 
    marks = int(Userdata.AverageMarks)
    data = []
    Joblist = Job.objects.filter(JObDept = dept, JobCrit__lte = cri , JobMarks__lte = marks)
    if Userdata.activeJobs == None:
        data = []
    else:
        ApplJobs = json_2_list(Userdata.activeJobs)
        for actjob in ApplJobs:
            JobData = Job.objects.filter(jobTitle=actjob)
            data.append(JobData[0])
        
    # JobCrit = cri, JobMarks = marks
    Joblist = list(set(list(Joblist)) - set(data))
    param={}
    if len(Joblist) == 0:
        param = {'Jobs' : 0}
    else:
        param = {'Jobs' : 1, 'JobList': Joblist}
    

    return render(request, "WEBAPP/StudentDash.html", param)


@login_required
def JobApply(request):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    if request.method == 'POST':
        applList = []
        applDt = []
        applStat = []
        JobTitle =  request.POST['job']
        JobData = Job.objects.filter(jobTitle=JobTitle)
        JobData = JobData[0]
        JobData.JobAppl = int(JobData.JobAppl) + 1
        if JobData.ApplList == None:
            applList = []
            

        else:
            applList = json_2_list(JobData.ApplList)
        applList.append(str(request.user))
        JobData.ApplList = list_2_json(applList)
        JobData.save()
        UserData = StudentProfile.objects.filter(StudentId = request.user)
        UserData = UserData[0]
        UserData.Appld_job = int(UserData.Appld_job) + 1
        if UserData.activeJobs == None:
            applList = []
            applDt = []
            applStat = []
        else:
            applList = json_2_list(UserData.activeJobs)
            applDt = json_2_list(UserData.AppDtJ)
            applStat = json_2_list(UserData.StatusJ)
        applList.append(str(JobTitle))
        applDt.append(str(d1))
        applStat.append(0)
        UserData.activeJobs = list_2_json(applList)
        UserData.StatusJ = list_2_json(applStat)
        UserData.AppDtJ = list_2_json(applDt)
        UserData.save()


        
        return redirect(StudentDash)


@login_required
def TrainApply(request):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    if request.method == 'POST':
        applList = []
        applDt = []
        applStat = []
        TrainTitle =  request.POST['train']
        TrainData = Training.objects.filter(TrainTitle=TrainTitle)
        TrainData = TrainData[0]
        TrainData.TrainAppl = int(TrainData.TrainAppl) + 1
        if TrainData.ApplList == None:
            applList = []
        else:
            applList = json_2_list(TrainData.ApplList)
        applList.append(str(request.user))
        TrainData.ApplList = list_2_json(applList)
        TrainData.save()
        UserData = StudentProfile.objects.filter(StudentId = request.user)
        UserData = UserData[0]
        UserData.Appld_Train = int(UserData.Appld_Train) + 1
        if UserData.activeTrains == None:
            applList = []
            applDt = []
            applStat = []
        else:
            applList = json_2_list(UserData.activeTrains)
            applDt = json_2_list(UserData.AppDtT)
            applStat = json_2_list(UserData.StatusT)
        applList.append(str(TrainTitle))
        applDt.append(str(d1))
        applStat.append(0)
        UserData.activeTrains = list_2_json(applList)
        UserData.StatusT = list_2_json(applStat)
        UserData.AppDtT = list_2_json(applDt)
        UserData.save()


        
        return redirect(StudentDashTrain)

@login_required
def StudentApplJob(request):
    Userdata = StudentProfile.objects.filter(StudentId = request.user)
    Userdata = Userdata[0]
    # applJobs = int(Userdata.Appld_job)
    
    data=[]
    StatusJ = []
    AppDtJ = []
    param ={}
    if Userdata.activeJobs == None:
        data = []
        StatusJ = []
        AppDtJ = []
    else:
        activeJobs = json_2_list(Userdata.activeJobs)
        StatusJ = json_2_list(Userdata.StatusJ)
        AppDtJ = json_2_list(Userdata.AppDtJ)
        for actjob in activeJobs:
            JobData = Job.objects.filter(jobTitle=actjob)
            data.append(JobData[0])
        
    if len(data)==0:
        param = {'mssg':1}
    else:
        data = zip(data,StatusJ,AppDtJ)
        param = {'mssg':0, 'data':data}
    return render(request, "WEBAPP/StudentApplJob.html", param)
    # return redirect(StudentDash)


@login_required
def StudentDashTrain(request):
    currentUser = request.user
    Userdata = StudentProfile.objects.filter(StudentId = currentUser)
    Userdata = Userdata[0]
    dept = Userdata.Department
    if Userdata.Semester == 0:
        cri = 0
    else:
        cri = int(Userdata.Semester) -1
        # 
    marks = int(Userdata.AverageMarks)
    data = []
    Trainlist = Training.objects.filter(TrainDept = dept, TrainCrit__lte = cri , TrainMarks__lte = marks)
    if Userdata.activeTrains == None:
        data = []
    else:
        ApplTrains = json_2_list(Userdata.activeTrains)
        for acttrain in ApplTrains:
            TrainData = Training.objects.filter(TrainTitle=acttrain)
            data.append(TrainData[0])
        
    # JobCrit = cri, JobMarks = marks
    Trainlist = list(set(list(Trainlist)) - set(data))
    param = {}
    if len(Trainlist) == 0:
        param = {'Jobs' : 0}
    else:
        param = {'Jobs' : 1, 'Trainlist': Trainlist}
    print(param)
    return render(request, "WEBAPP/StudentDashTrain.html", param)


@login_required
def StudentApplTrain(request):
    Userdata = StudentProfile.objects.filter(StudentId = request.user)
    Userdata = Userdata[0]
    # applJobs = int(Userdata.Appld_job)
    
    data=[]
    StatusT = []
    AppDtT = []
    param ={}
    if Userdata.activeTrains == None:
        data = []
        StatusT = []
        AppDtT = []
    else:
        activeTrain = json_2_list(Userdata.activeTrains)
        StatusT = json_2_list(Userdata.StatusT)
        AppDtT = json_2_list(Userdata.AppDtT)
        for actTrain in activeTrain:
            TrainData = Training.objects.filter(TrainTitle=actTrain)
            data.append(TrainData[0])
    if len(data)==0:
        param = {'mssg':1}
    else:
        data = zip(data,StatusT,AppDtT)
        param = {'mssg':0, 'data':data}
    return render(request, "WEBAPP/StudentApplTrain.html", param)

#############################################################################################################
######################################## COMPANY AREA ######################################################
###########################################################################################################
@login_required
def CompanyData(request):
    if request.method == 'POST':
        user = Company.objects.filter(CompanyId = request.user)
        user = user[0]
        user.CompanyNm =  request.POST['CompanyNm']
        user.Cmnyimage = request.FILES['Cmnyimage']
        user.ComPort = request.FILES['ComPort']
        user.ComAdd = request.POST['ComAdd']
        user.Web = request.POST['Web']
        user.FromFilld = 1
        user.save()
        return redirect(CompanyDash)



@login_required
def CompanyDash(request):
    companyname=Company.objects.filter(CompanyId=request.user)
    companyname=companyname[0]
    param= {}
    Joblist = Job.objects.filter(Company=companyname.CompanyNm)
    if len(Joblist) == 0:
        param = {'mssge':0}
    else:
        
        L_data = []
        LaccptData = []
        accptData = []
        for jobdata in Joblist:
            data = []
            LaccptData = []
            accptData = []
            if jobdata.ApplList == None:
                data.append('none')
            else:
                for list_name in json_2_list(jobdata.ApplList):
                    userData = StudentProfile.objects.filter(StudentId=list_name)
                    userData = userData[0]
                    JobSet = json_2_list(userData.activeJobs)
                    accptSet = json_2_list(userData.StatusJ)
                    for i in range(len(accptSet)):
                        if JobSet[i] == str(jobdata.jobTitle):
                            accptData.append(accptSet[i])    
                    data.append(userData)
            LaccptData = zip(accptData,data)    
            L_data.append(LaccptData)  
            # LaccptData.append(accptData)  

        Joblist = zip(list(Joblist),L_data)
        param = {'Joblist':Joblist,'mssge':1, 'Fdata':"none"}
        
    return render(request, "WEBAPP/ComDash.html", param)

@login_required
def ComTrainDash(request):
    companyname=Company.objects.filter(CompanyId=request.user)
    companyname=companyname[0]
    param= {}
    Trainlist = Training.objects.filter(Company=companyname.CompanyNm)
    if len(Trainlist) == 0:
        param = {'mssge':0}
    else:
        L_data = []
        LaccptData = []
        accptData = []
        for traindata in Trainlist:
            data = []
            LaccptData = []
            accptData = []
            if traindata.ApplList == None:
                data.append('none')
            else:
                for list_name in json_2_list(traindata.ApplList):
                    userData = StudentProfile.objects.filter(StudentId=list_name)
                    userData = userData[0]
                    TrainSet = json_2_list(userData.activeTrains)
                    accptSet = json_2_list(userData.StatusT)
                    for i in range(len(accptSet)):
                        if TrainSet[i] == str(traindata.TrainTitle):
                            accptData.append(accptSet[i])   
                    data.append(userData)
            LaccptData = zip(accptData,data)  
            L_data.append(LaccptData)    

        Trainlist = zip(list(Trainlist),L_data)
        param = {'Trainlist':Trainlist,'mssge':1, 'Fdata':"none"}

    return render(request, "WEBAPP/ComTrainDash.html", param)

@login_required
def ComJobcreate(request):
    return render(request, "WEBAPP/ComJobcreate.html")

@login_required
def ComTraincreate(request):
    return render(request, "WEBAPP/ComTraincreate.html")

@login_required
def CreateJob(request):
    if request.method == 'POST':
        CompanyUser = Company.objects.filter(CompanyId =request.user)
        CompanyUser = CompanyUser[0]
        JobData = Job.objects.filter(jobTitle = request.POST['jobTitle'])
        
        if len(JobData) == 0:
            JobData = Job(jobTitle = request.POST['jobTitle'], jobDesc = request.POST['jobDesc'], JobCrit = request.POST['JobCrit'], JobMarks = request.POST['JobMarks'], JObDept = request.POST['JObDept'], Company = CompanyUser.CompanyNm)
            JobData.save()
            param = {'Status':1}
        else:
            param = {'Status':2}
        return render(request, "WEBAPP/ComJobcreate.html",param)

    else:    
        param = {'Status':2}
        return render(request, "WEBAPP/ComJobcreate.html",param)
@login_required
def JobDelete(request):
    if request.method == 'POST':
        JobTitle = request.POST['job']
        JobData = Job.objects.filter(jobTitle = JobTitle)
        JobData = JobData[0]
        data = []
        data.append(JobTitle)
        if JobData.ApplList == None:
            JobData.delete()
        else:
            applList = json_2_list(JobData.ApplList)
            for userApp in applList:
                userData = StudentProfile.objects.filter(StudentId = userApp)
                userData = userData[0]
                if len(json_2_list(userData.activeJobs)) == 1:
                    userData.activeJobs = None
                    userData.StatusJ = None
                    userData.AppDtJ = None
                    userData.Appld_job = int(userData.Appld_job) - 1
                    userData.save()
                else:
                    jobList = json_2_list(userData.activeJobs)
                    accpDT = json_2_list(userData.AppDtJ)
                    statLst = json_2_list(userData.StatusJ)
                    for i in range(len(jobList)):
                        if jobList[i] == JobTitle:
                            accpDT.pop(i)
                            statLst.pop(i)  
                    userData.AppDtJ = list_2_json(accpDT)
                    userData.StatusJ = list_2_json(statLst)
                    userData.activeJobs = list_2_json(list(set(jobList) - set(data)))
                    userData.Appld_job = int(userData.Appld_job) - 1
                    userData.save()
                
            JobData.delete()
    return redirect(CompanyDash)

@login_required
def TrainDelete(request):
    if request.method == 'POST':
        TrainTitle = request.POST['train']
        TrainData = Training.objects.filter(TrainTitle = TrainTitle)
        TrainData = TrainData[0]
        data = []
        data.append(TrainTitle)
        if TrainData.ApplList == None:
            TrainData.delete()
        else:
            applList = json_2_list(TrainData.ApplList)
            for userApp in applList:
                userData = StudentProfile.objects.filter(StudentId = userApp)
                userData = userData[0]
                if len(json_2_list(userData.activeTrains)) == 1:
                    userData.activeTrains = None
                    userData.StatusT = None
                    userData.AppDtT = None
                    userData.Appld_Train = int(userData.Appld_Train) - 1
                    userData.save()
                else:
                    accpDT = json_2_list(userData.AppDtJ)
                    statLst = json_2_list(userData.StatusJ)
                    TrainList = json_2_list(userData.activeTrains)
                    for i in range(len(TrainList)):
                        if TrainList[i] == TrainTitle:
                            accpDT.pop(i)
                            statLst.pop(i)
                    userData.AppDtT = list_2_json(accpDT)
                    userData.StatusT = list_2_json(statLst)
                    userData.activeTrains = list_2_json(list(set(TrainList) - set(data)))
                    userData.Appld_Train = int(userData.Appld_Train) - 1
                    userData.save()
                
            TrainData.delete()
    return redirect(CompanyDash)


@login_required
def CreateTrain(request):
    if request.method == 'POST':
        CompanyUser = Company.objects.filter(CompanyId =request.user)
        CompanyUser = CompanyUser[0]
        TrainData = Training.objects.filter(TrainTitle = request.POST['TrainTitle'])
        if len(TrainData) == 0:
            TrainData = Training(TrainTitle = request.POST['TrainTitle'], TrainDesc = request.POST['TrainDesc'], TrainCrit = request.POST['TrainCrit'], TrainMarks = request.POST['TrainMarks'], TrainDept = request.POST['TrainDept'], Company = CompanyUser.CompanyNm)
            TrainData.save()
            param = {'Status':1}
        else:
            param = {'Status':2}
        return render(request, "WEBAPP/ComTraincreate.html",param)
    else:    
        param = {'Status':2}
        return render(request, "WEBAPP/ComTraincreate.html",param)

#     return render(request, "WEBAPP/ComForm.html")ComTraincreate.html


@login_required
def JobAccpt(request):
    if request.method == 'POST':
        JobTitle = request.POST['job']
        studid = request.POST['studid']
        studData = StudentProfile.objects.filter(StudentId = studid)
        studData = studData[0]
        data = []
        data.append(JobTitle)
        Jobset = json_2_list(studData.activeJobs)
        Jaccpt = json_2_list(studData.StatusJ)
        for i in range(len(Jobset)):
            if Jobset[i] == JobTitle:
                Jaccpt[i]=1
        studData.StatusJ = list_2_json(Jaccpt)
        studData.save()
    return redirect(CompanyDash)


    # 
@login_required
def JobRjt(request):
    if request.method == 'POST':
        JobTitle = request.POST['job']
        studid = request.POST['studid']
        studData = StudentProfile.objects.filter(StudentId = studid)
        studData = studData[0]
        data = []
        data.append(JobTitle)
        Jobset = json_2_list(studData.activeJobs)
        Jaccpt = json_2_list(studData.StatusJ)
        for i in range(len(Jobset)):
            if Jobset[i] == JobTitle:
                Jaccpt[i]=2
        studData.StatusJ = list_2_json(Jaccpt)
        studData.save()
    return redirect(CompanyDash)


@login_required
def TrainAccpt(request):
    if request.method == 'POST':
        TrainTitle = request.POST['train']
        studid = request.POST['studid']
        studData = StudentProfile.objects.filter(StudentId = studid)
        studData = studData[0]
        data = []
        data.append(TrainTitle)
        Trainset = json_2_list(studData.activeTrains)
        Taccpt = json_2_list(studData.StatusT)
        for i in range(len(Trainset)):
            if Trainset[i] == TrainTitle:
                Taccpt[i]=1
        studData.StatusT = list_2_json(Taccpt)
        studData.save()
    return redirect(CompanyDash)


    # 
@login_required
def TrainRjt(request):
    if request.method == 'POST':
        TrainTitle = request.POST['train']
        studid = request.POST['studid']
        studData = StudentProfile.objects.filter(StudentId = studid)
        studData = studData[0]
        data = []
        data.append(TrainTitle)
        Trainset = json_2_list(studData.activeTrains)
        Taccpt = json_2_list(studData.StatusT)
        for i in range(len(Trainset)):
            if Trainset[i] == TrainTitle:
                Taccpt[i]=2
        studData.StatusT = list_2_json(Taccpt)
        studData.save()
    return redirect(CompanyDash)

# jobTitle = models.CharField(max_length=50,default="")
    # jobDesc = models.CharField(max_length=250,default="")
    # JobCrit = models.CharField(max_length=50,default="")
    # JobMarks = models.IntegerField(default=0)
    # JObDept = models.CharField(max_length=50,default="")
    # Company = models.CharField(max_length=50,default="")
    # JobAppl = models.IntegerField(default=0)