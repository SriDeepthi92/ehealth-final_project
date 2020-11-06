import django_tables2 as tables
from ..models import AllData
from django.shortcuts import render

def table(request):
    data = AllData.objects.all()
    return render(request, 'clinic/students/list.html', locals())
