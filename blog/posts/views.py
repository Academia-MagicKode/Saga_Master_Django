from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.


def detail_view(request, id):
    return HttpResponse()

def posts_view(request):
    return HttpResponse("Wellcome to posts")

def by_year_posts(request, year, month):
    return HttpResponse("BY year view"+str(year) +str(month))