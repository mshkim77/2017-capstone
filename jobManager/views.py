from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Job

@csrf_exempt
def get_job_status(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return JsonResponse({"job_status": job.status, "last_update": job.last_update})