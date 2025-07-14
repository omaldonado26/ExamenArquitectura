from django.shortcuts import render

# Create your views here.
# sistema/views.py

from django.shortcuts import render
from .utils.system_info import (
    get_cpu_usage,
    get_memory_info,
    get_disk_info,
    get_system_info
)

def status(request):
    context = {
        'cpu':    get_cpu_usage(),
        'memory': get_memory_info(),
        'disk':   get_disk_info(),
        'system': get_system_info(),
    }
    return render(request, 'sistema/status.html', context)
