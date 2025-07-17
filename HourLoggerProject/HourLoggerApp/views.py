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
    logs = Log.objects.all()
    total = 0
    for log in logs:
        total += log.sumTime
    totalHours = secondsToTime(total)

    jobs = Job.objects.all()
    context = {
        "totalHours": totalHours,
        "logs": logs,
        "jobs": jobs
    }
    return render(request, "showLogs.html", context)

def updateTable(request, *args, **kwargs):
    print(request.GET)
    job = request.GET.get('job')
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    if startDate != '':
        logs = Log.objects.filter(date>=startDate)
    logs = Log.objects.filter(job=job)
    total = 0
    for log in logs:
        total += log.sumTime
    totalHours = secondsToTime(total)

    context = {
        "totalHours": totalHours,
        "logs": logs,
    }
    return render(request, "partials/logTable.html", context)

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

    partOfDay = "AM"

    if int(hours) >= 12:
        partOfDay = "PM"
    hoursNormal = int(hours) % 12
    if hoursNormal == 0:
        hoursNormal = 12
    
    seconds = seconds.split(".")[0]

    formattedTime = f"{hoursNormal}:{minutes}:{seconds} {partOfDay}"

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

def secondsToTime(duration):
    newHours = duration // 3600

    duration -= (newHours*3600)

    if newHours < 10:
        newHours = f"0{newHours}"

    newMin = duration//60

    duration -= (newMin*60)

    if newMin < 10:
        newMin = f"0{newMin}"

    newSeconds = duration

    if newSeconds < 10:
        newSeconds = f"0{newSeconds}"

    newDuration = f"{newHours}:{newMin}:{newSeconds}"

    return newDuration
