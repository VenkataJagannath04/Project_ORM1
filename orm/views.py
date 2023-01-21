from django.shortcuts import render
from orm.models import *
from django.http import HttpResponse
# Create your views here.

def insert_course(request):
    cn = input('Enter Course name: ')
    C = Course.objects.get_or_create(Cname = cn)[0]
    C.save()
    return HttpResponse('Course name inserted successfully!')

def insert_website(request):
    cn = input('Enter Course name: ')
    sn = input('Enter Student name: ')
    url = input('Enter url: ')
    C = Course.objects.get_or_create(Cname = cn)[0]
    C.save()
    S = Website.objects.get_or_create(Cname = C, Sname = sn, url = url)[0]
    S.save()
    return HttpResponse('Website details inserted successfully!')

def insert_access(request):
    cn = input('Enter Course name: ')
    sn = input('Enter Student name: ')
    url = input('Enter url: ')
    dt = input('Enter date:')
    C = Course.objects.get_or_create(Cname = cn)[0]
    C.save()
    S = Website.objects.get_or_create(Cname = C, Sname = sn, url = url)[0]
    S.save()
    D = AccessRecord.objects.get_or_create(Sname = S, Date = dt)[0]
    D.save()
    return HttpResponse('Access Records inserted successfully!')
