from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def main(request):
    return render(request,'index.html')
