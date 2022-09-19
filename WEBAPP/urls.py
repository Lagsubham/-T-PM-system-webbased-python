from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login_site, name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
    path('StudentDash/', views.StudentDash, name='StudentDash'),
    path('CompanyDash/', views.CompanyDash, name='CompanyDash'),
    path('FromFillup/', views.FromFillup, name='FromFillup'),
    path('SemSel/', views.SemSel, name='SemSel'),
    path('ComJobcreate/', views.ComJobcreate, name='ComJobcreate'),
    path('ComTraincreate/', views.ComTraincreate, name='ComTraincreate'),
    path('ComTrainDash/', views.ComTrainDash, name='ComTrainDash'),
    path('CompanyData/', views.CompanyData, name='CompanyData'),
    path('CreateJob/', views.CreateJob, name='CreateJob'),
    path('CreateTrain/', views.CreateTrain, name='CreateTrain'),
    path('StudentDashTrain/', views.StudentDashTrain, name='StudentDashTrain'),
    path('JobApply/', views.JobApply, name='JobApply'),
    path('StudentApplJob/', views.StudentApplJob, name='StudentApplJob'),
    path('StudentApplTrain/', views.StudentApplTrain, name='StudentApplTrain'),
    path('TrainApply/', views.TrainApply, name='TrainApply'),
    path('JobDelete/', views.JobDelete, name='JobDelete'),
    path('TrainDelete/', views.TrainDelete, name='TrainDelete'),
    path('JobAccpt/', views.JobAccpt, name='JobAccpt'),
    path('JobRjt/', views.JobRjt, name='JobRjt'),
    path('TrainAccpt/', views.TrainAccpt, name='TrainAccpt'),
    path('TrainRjt/', views.TrainRjt, name='TrainRjt'),


    # path('comform/', views.comform, name='comform'),
    # path('SemSelP/', views.SemSelP, name='SemSelP'),ComJobcreate

    # path('about/', views.about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('tracker/', views.tracker, name='tracker'),
    # path('search/', views.search, name='search'),
    # path('productView/', views.productView, name='productView'),
    # path('checkout/', views.checkout, name='checkout'),
    
    path('logout/', views.logout_site, name='logout'),
    
    # path('DASH/', views.DASH, name='DASH'),
]
