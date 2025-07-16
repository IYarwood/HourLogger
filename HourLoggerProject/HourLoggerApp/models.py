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

    class Meta:
        db_table = "Logs"
