
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from .forms import SignInForm
from .forms import SignUpForm
from .models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.db.models import Sum
import razorpay
from groceryshop.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
# Create your views here.
def index(request):
    return render(request,'base.html')
# Create your views here.
def product(request):
    data = Product.objects.all()
    return render(request,'product.html',{"data":data})
def signup(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SignUpForm()
    return render(request,'signup.html',{'form':fm})
# Create your views here.

def about(request):
    return render(request,"about.html")
def signin(request):
    if request.method=="POST":
        fm=SignInForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return redirect("/")
    else:
        fm=SignInForm()
    return render(request,'signin.html',{'form':fm})
@login_required(login_url="signin")
def signout(request):
    logout(request)
    return redirect('/')

@login_required(login_url="signin")
def cart(request):
    # print("user")
    client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
    #print(request.POST)
    
    order_currency = 'INR'
    data = Cart.objects.all()
    print(data)

    total_price = Cart.objects.filter(user=request.user).aggregate(Sum('price'))
    return render(request,"cart.html",{"cart":data,"total_price": total_price["price__sum"],'api_key':RAZORPAY_API_KEY,'api_secret_key':RAZORPAY_API_SECRET_KEY})

def add_to_cart(request, id):
    #print(request.user.id)
    data = Product.objects.filter(id=id)
    for product in data:
        Cart(user= request.user, name = product.name, price = product.price, image = product.image, unit = product.unit).save()
    return redirect("/product/")

def remove_from_cart(request, id):
    Cart.objects.filter(id=id).delete()
    # total_price = Cart.objects.aggregate(Sum('price'))
    # return render(request, "cart.html",total_price)
    return redirect("/cart/")

def search(request):
    data = Product.objects.filter(name=request.POST.get("name"))
    # print("data")
    # print(request.POST.get("name"))
    return render(request,"product.html",{"data":data})   


