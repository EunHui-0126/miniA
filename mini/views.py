from django.http import HttpResponse
from django.http import HttpResponseRedirect
<<<<<<< HEAD

from django.shortcuts import render, redirect

=======
>>>>>>> ea8b46f6fa121f3d96f4fbc3f0383b8335cdd5a8
from django.shortcuts import render, redirect
from app.models import Article
from django.shortcuts import render
from django.http import JsonResponse # JSON 응답
from app.models import phone
from django.forms.models import model_to_dict

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
    return render(request,'index.html',{'data':data})

# def phone_data(request):
#     data = phone.objects.all()
#     phone_list = []
#     for p in data:
#         d = model_to_dict(p) # QuerySet -> Dict
#         phone_list.append(d)
<<<<<<< HEAD
#     return JsonResponse(phone_list, safe=False)
=======
#     return JsonResponse(phone_list, safe=False)
>>>>>>> ea8b46f6fa121f3d96f4fbc3f0383b8335cdd5a8
