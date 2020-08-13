from django.http import HttpResponse
from django.http import HttpResponseRedirect


from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from app.models import Article
from django.shortcuts import render
from django.http import JsonResponse # JSON 응답
from app.models import phone
from app.models import menu
from django.forms.models import model_to_dict
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
    address = 'http://www.andong.ac.kr/main/module/foodMenu/view.do?manage_idx=21&memo5=2020-08-13'
    res = requests.get(address)
    soup = bs(res.text,'html.parser')
    a_list = soup.select_one('dl:nth-child(2)')
    data = phone.objects.all()

    return render(request,'index.html',{'a_list':a_list.get_text('"\n"'),'data':data})


def phone_data(request):
    data = phone.objects.all()
    return render(request,'index.html',{'data':data})
    


    i=random.randint(1,43)
    r=menu.objects.get(id=i)
    return render(request,'index.html',{'a_list':a_list.get_text('"\n"'),'data':data,'r':r})
