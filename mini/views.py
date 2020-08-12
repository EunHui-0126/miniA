from django.http import HttpResponse
from django.http import HttpResponseRedirect
<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
<<<<<<< HEAD
from django.shortcuts import render, redirect

# from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from article.models import Blog
from app.models import Article

def main(request):
    return render(request,'base.html')

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

 
=======
from django.shortcuts import render
>>>>>>> ed86002b9fb9519619df34a38a96e484454a41da
from django.http import JsonResponse # JSON 응답
from app.models import phone
from django.forms.models import model_to_dict


# from django.shortcuts import render, get_object_or_404, redirect
# from django.utils import timezone
# from article.models import Blog
from app.models import Article

def main(request):
    return render(request,'base.html')

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
    return render(request,'index.html')

def phone_data(request):
    data = phone.objects.all()
    return render(request,'base.html',{'data':data})

# def phone_data(request):
#     data = phone.objects.all()
#     phone_list = []
#     for p in data:
#         d = model_to_dict(p) # QuerySet -> Dict
#         phone_list.append(d)
#     return JsonResponse(phone_list, safe=False)
<<<<<<< HEAD

=======
>>>>>>> ccba940326267a055ed417fbb2a7d7d3449f3776
>>>>>>> ed86002b9fb9519619df34a38a96e484454a41da
