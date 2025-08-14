from django.db import models
from datetime import date

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Jobs"

class Log(models.Model):
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name="Logs")
    date = models.DateField(default=date.today)
    start = models.CharField(max_length=20, verbose_name="Start")
    end = models.CharField(max_length=20, verbose_name="End")

    @property
    def duration(self):
        def convertToMilitary(hour, partOfDay):
            hour = int(hour)
            if partOfDay == "AM" and hour == 12:
                return 0
            elif partOfDay == "PM" and hour != 12:
                return hour + 12
            else:
                return hour
        start = self.start
        startHour, startMin, startSec = start.split(":")
        startSec, partOfDay = startSec.split(" ")

        militaryStartTime = convertToMilitary(startHour, partOfDay)


        end = self.end
        endHour, endMin, endSec = end.split(":")
        endSec, partOfDay = endSec.split(" ")

        militaryEndTime = convertToMilitary(endHour, partOfDay)

        totalStart = (int(militaryStartTime)*3600) + (int(startMin)*60) + int(startSec)

        totalEnd = (int(militaryEndTime)*3600) + (int(endMin)*60) + int(endSec)

        if totalEnd < totalStart:
            totalEnd += 24 * 3600

        duration = totalEnd - totalStart

        newHours = duration // 3600

        duration -= (newHours*3600)

        newMin = duration//60

        duration -= (newMin*60)

        newSeconds = duration

        newDuration = f"{newHours:02}:{newMin:02}:{newSeconds:02}"

        return newDuration

    @property
    def sumTime(self):
        def convertToMilitary(hour, partOfDay):
            hour = int(hour)
            if partOfDay == "AM" and hour == 12:
                return 0
            elif partOfDay == "PM" and hour != 12:
                return hour + 12
            else:
                return hour
            
        start = self.start
        startHour, startMin, startSec = start.split(":")
        startSec, partOfDay = startSec.split(" ")

        militaryStartTime = convertToMilitary(startHour, partOfDay)


        end = self.end
        endHour, endMin, endSec = end.split(":")
        endSec, partOfDay = endSec.split(" ")

        militaryEndTime = convertToMilitary(endHour, partOfDay)

        totalStart = (int(militaryStartTime)*3600) + (int(startMin)*60) + int(startSec)

        totalEnd = (int(militaryEndTime)*3600) + (int(endMin)*60) + int(endSec)

        if totalEnd < totalStart:
            totalEnd += 24 * 3600

        duration = totalEnd - totalStart

        return duration



    class Meta:
        db_table = "Logs"
