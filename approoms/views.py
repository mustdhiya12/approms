from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "app/dastyle_v1.1/index.html",{
        "name":"Muhammad Fauzan Nur Ilham", 
        "greet":"Assalamualaikum", 
        "head":"App rooms", 
        "header":"header", 
        "footer":"footer", 
    })