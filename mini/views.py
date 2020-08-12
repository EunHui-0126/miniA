from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse # JSON 응답
from app.models import phone
from django.forms.models import model_to_dict


def main(request):
    return render(request,'index.html')

def phone_data(request):
    data = phone.objects.all()
    return render(request,'index.html',{'data':data})

# def phone_data(request):
#     data = phone.objects.all()
#     phone_list = []
#     for p in data:
#         d = model_to_dict(p) # QuerySet -> Dict
#         phone_list.append(d)
#     return JsonResponse(phone_list, safe=False)
