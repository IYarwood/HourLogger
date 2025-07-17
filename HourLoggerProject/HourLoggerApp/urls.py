from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.jobSelect, name="jobSelect"),
    path("timerPage/", views.timerPage, name="timerPage"),
    path("showLogs/", views.showLogs, name="showLogs"),
    path("getTime/", views.getTime, name="getTime"),
    path("createLog/", views.createLog, name="createLog"),
    path("updateTable/", views.updateTable, name="updateTable"),
]

    
    

