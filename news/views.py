from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import News
from django.shortcuts import redirect, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import personDetails
from django.http import JsonResponse
import json
from django.db.models import Q
from django.db import IntegrityError

# Create your views here.


def signin(request):
     if (request.method=='GET'):
        return render(request,'login.html')
     else:
    # if request.method == "POST"
        # next_url = request.POST.get('next')
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u,password=p)
        print(user)
        try:
            if user.is_staff:
                login(request,user)
                return redirect('home')
        except:
            messages.add_message(request, messages.ERROR, "passsword match vayena")
            return redirect('signin')



        # if user is not None:
        #     messages.success(request, 'Login Successful', extra_tags='success')
        #     # if next_url:
        #     #     next_url = request.POST.get('home')
        #     return redirect('home')
        # else:
        #     messages.add_message(request, messages.ERROR, "passsword match vayena")
        #     return redirect('signin')



def signup(request):
    if (request.method=='GET'):
        return render(request,'signup.html')
    else:
        u = request.POST['username']
        e = request.POST['email']
        p1 = request.POST['password']
        p2 = request.POST["cpassword"]

        if (p1==p2):
            u = User(username=u,email=e)
            u.set_password(p1)
            u.save()
            messages.add_message(request, messages.SUCCESS, "sign up succcess")
            return redirect('news:signin')
        else:
           
            messages.add_message(request, messages.ERROR, "babu password match huney gari hana na")
            return redirect('signup')


def signout(request):
    logout(request)
    return redirect('signin')


# @login_required(login_url='signin')
def home(request):
    if not request.user.is_staff:
        return redirect('signin')
    li = News.objects.all()
    return render(request,'home.html',{'li':li})


 


# @login_required(login_url='signin')
def detail(request,id):
    prod = get_object_or_404(News,id=id)
    return render(request,'details.html',{"prod":prod})


# def search(request):
#   query = request.GET.get('q')
#   posts = News.objects.filter(Q(title__icontains=query))
#   if not posts :
#     posts = ""
#   return render(request, 'posts/posts.html', {'posts': posts})

# @login_required(login_url='signin')
def search(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = News.objects.filter(title__contains=query_name)
            return render(request, 'news-search.html', {"results":results})

    return render(request, 'news-search.html')




def index(request):
        #data = serializers.serialize("json",personDetails.objects.all(),fields=('email','password'))
		data=list(personDetails.objects.all())
		dict1 ={}
		for i in data:
			dict1[i.email] = i.password
		json1  = json.dumps(dict1,sort_keys=True)
		return render(request,'loginPage.html',{'personObject':json1})



def registration(request):
	if request.method=='POST':
		if (request.POST.get('name') and request.POST.get('email') and request.POST.get('phonenumber') and request.POST.get('password')):
			post=personDetails()
			post.name=request.POST.get('name')
			post.email=request.POST.get('email')
			post.phonenumber=request.POST.get('phonenumber')
			post.password=request.POST.get('password')
			check= {
        		"variable": "0"
			}
			json2 =json.dumps(check,sort_keys=True)
			try:
				post.save()
				return render(request,'loginPage.html')
			except IntegrityError as e:
				check["variable"]="1"
				json2 =json.dumps(check,sort_keys=True)
				return render(request,'registrationPage.html',{'validator':json2})
	else:
		return render(request,'registrationPage.html')



# def login(request):
#     if (request.method=='GET'):
#         return render(request,'loginPage.html')
#     else:
         
#         u = request.POST['username']
#         p = request.POST['password']
#         user = authenticate(name=u,password=p)
#         print(user)
#         if user is not None:
#             messages.success(request, 'Login Successful', extra_tags='success')
#             return redirect('news:home')
#         else:
#             messages.add_message(request, messages.ERROR, "passsword match vayena")
#             return redirect('news:signin')


def cards(request):
	return render(request,'cards.html')



def about(request):
    return render(request,"about.html")



 