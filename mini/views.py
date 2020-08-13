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

def base(request):
    return render(request,'base.html')

def update(request, id):
    # select * from article where id = ?
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        try:
            # update article set title = ?, content = ? where id = ?
            article.title = title
            article.content = content
            article.save()
            return render(request, 'update_success.html')
        except:
            return render(request, 'update_fail.html')
    context = {
        'article' : article
    }
    return render(request, 'update.html', context)


def detail(request, id):
# select * from article where id = ?
    article = Article.objects.get(id=id)
    context = {
        'article' : article
    }
    return render(request, 'detail.html', context)

def delete(request, id):
    try:
    # select * from article where id = ?
        article = Article.objects.get(id=id)
        article.delete()
        return render(request, 'delete_success.html')
    except:
        return render(request, 'delete_fail.html')