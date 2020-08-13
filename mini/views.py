from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from app.models import Article
from django.shortcuts import render
from django.http import JsonResponse # JSON 응답
from app.models import phone
from app.models import menu
from django.forms.models import model_to_dict

from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
import datetime
import requests
from bs4 import BeautifulSoup as bs
import random
from app.models import Point
from django.forms.models import model_to_dict


def board(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # email = request.session['email']
            # # select * from user where email = ?
            # user = User.objects.get(email=email)
            # # insert into article (title, content, user_id) values (?, ?, ?)
            article = Article(title=title, content=content)
            article.save()
            return redirect('/list')
        except:
            return render(request, 'base.html')
    # return render(request, 'write.html')
    return render(request,'create.html')

def list(request):
    article_list = Article.objects.order_by('-id')
    print(article_list)
    context = {
        'article_list' : article_list
    }
    return render(request,'list.html', context)


def main(request):
    address = cur_date_address()
    res = requests.get(address)
    soup = bs(res.text,'html.parser')
    a_list = soup.select_one('dl:nth-child(2)')
    data = phone.objects.all()
    i=random.randint(1,43)
    r=menu.objects.get(id=i)
    return render(request,'index.html',{'a_list':a_list.get_text('"\n"'),'data':data,'r':r})
    
def phone_data(request):
    data = phone.objects.all()
    return render(request,'index.html',{'data':data})

def cur_date_address():
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    parts = urlparse('http://www.andong.ac.kr/main/module/foodMenu/view.do?manage_idx=21&memo5=2020-08-12')
    qs = dict(parse_qsl(parts.query))
    qs['memo5'] = nowDate
    parts = parts._replace(query=urlencode(qs))
    address = urlunparse(parts)
    return address


def phone_data(request):
    data = phone.objects.all()
    return render(request,'index.html',{'data':data})

def map(request):
    return render(request, 'main.html')

def map_data(request):
    data = Point.objects.all()
    map_list = []
    for d in data:
        d = model_to_dict(d) # QuerySet -> Dict
        map_list.append(d)
    # dict가 아닌 자료는 항상 safe=False 옵션 사용
    return JsonResponse(map_list, safe=False)