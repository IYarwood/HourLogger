from django.shortcuts import render
from .models import Job, Log
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def jobSelect(request, *args, **kwargs):
    jobs = Job.objects.all()

    context = {
        "jobs": jobs,
    }

    return render(request, "jobSelect.html", context)

def showLogs(request, *args, **kwargs):
    return render(request, "showLogs.html")

def timerPage(request, *args, **kwargs):
    jobID = request.GET.get('job')
    context = {
        "jobID": jobID
    }
    return render(request, "timerPage.html", context)

@api_view(['GET'])
def getTime(request):
    now = datetime.now() 
    currentTime = str(now.time())
    
    hours, minutes, seconds = currentTime.split(":")

    hoursNormal = int(hours) % 12
    if hoursNormal == 0:
        hoursNormal = 12
    
    seconds = seconds.split(".")[0]

    formattedTime = f"{hoursNormal}:{minutes}:{seconds}"

    return Response({'time': formattedTime})

@api_view(['GET'])
def createLog(request, *args, **kwargs):
    print(request.GET)
    start = request.GET.get('start')
    stop = request.GET.get('stop')
    jobID = int(request.GET.get('jobID'))
    job = Job.objects.get(pk=jobID)
    Log.objects.create(job=job, start=start, end=stop)
    return Response({'status': "Submitted"})