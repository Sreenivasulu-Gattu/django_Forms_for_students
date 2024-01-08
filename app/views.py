from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def school(request):
    ESFO = SchoolForm()
    d = {'DATA':ESFO}

    if request.method == 'POST':
        ESFO = SchoolForm(request.POST)
        if ESFO.is_valid():
            sn = ESFO.cleaned_data['sname']
            SO = School.objects.get_or_create(sname = sn)[0]
            SO.save()
            return HttpResponse(str(ESFO.cleaned_data))
        else:
            return HttpResponse('Data Invalid')
    return render(request,'school.html',d)