from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "Jobs"

class Log(models.Model):
    job = models.ForeignKey(Job, on_delete=models.PROTECT, verbose_name="Logs")
    date = models.DateField(auto_now_add=True)
    start = models.CharField(max_length=20, verbose_name="Start")
    end = models.CharField(max_length=20, verbose_name="End")

    @property
    def duration(self):
        start = self.start
        startHour, startMin, startSec = start.split(":")
        startSec, partOfDay = startSec.split(" ")

        militaryStartTime = 0
        if partOfDay == "PM":
            militaryStartTime = 12 + int(startHour)


        end = self.end
        endHour, endMin, endSec = end.split(":")
        endSec, partOfDay = endSec.split(" ")

        militaryEndTime = 0
        if partOfDay == "PM":
            militaryEndTime = 12 + int(endHour)

        totalStart = (int(militaryStartTime)*3600) + (int(startMin)*60) + int(startSec)

        totalEnd = (int(militaryEndTime)*3600) + (int(endMin)*60) + int(endSec)

        duration = totalEnd - totalStart

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

    @property
    def sumTime(self):
        start = self.start
        startHour, startMin, startSec = start.split(":")
        startSec, partOfDay = startSec.split(" ")

        militaryStartTime = 0
        if partOfDay == "PM":
            militaryStartTime = 12 + int(startHour)


        end = self.end
        endHour, endMin, endSec = end.split(":")
        endSec, partOfDay = endSec.split(" ")

        militaryEndTime = 0
        if partOfDay == "PM":
            militaryEndTime = 12 + int(endHour)

        totalStart = (int(militaryStartTime)*3600) + (int(startMin)*60) + int(startSec)

        totalEnd = (int(militaryEndTime)*3600) + (int(endMin)*60) + int(endSec)

        duration = totalEnd - totalStart

        return duration



    class Meta:
        db_table = "Logs"
