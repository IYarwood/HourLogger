from django.shortcuts import render
from .models import Job, Log

# Create your views here.
def jobSelect(request, *args, **kwargs):
    jobs = Job.objects.all()
    fields = Job._meta.fields

    context = {
        "jobs": jobs,
    }

    return render(request, "jobSelect.html", context)