from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import WatcheDB,watchupload,wishlist,Cart,Watchreviews
from  . forms import uploadforms
from django.contrib.auth.decorators import login_required

# Create your views here.




def Home(request):
    watches = watchupload.objects.all()
    context={"watches_t":watches}
    return render(request, 'home.html', context)

@login_required(login_url='login')
def upload(request):
    if request.method == "POST":
        form = uploadforms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = uploadforms()

    return render(request, "upload.html", {'form': form})



def about(request):
    return render(request,'about.html')

from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout

def login_page(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')

            user=authenticate(username=user_name,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        return render(request,'login_page.html',{'form':form})
    else:
        form=AuthenticationForm()
    return render(request,'login_page.html',{'form':form})


def signup_page(request):
    if request.method=="POST":
        form=UserCreationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
        
    return render(request,'signup.html',{'form':form})


def logout_page(request):
    logout(request)
    return redirect('home')

from django.shortcuts import get_object_or_404
def show_product(request,id):
    product = get_object_or_404(watchupload,id=id)
    review_obj=Watchreviews.objects.filter(products=product)
    return render(request,'product.html',{'product':product,'reviews':review_obj})


def addtowish(request,id):
    user = request.user
    product = watchupload.objects.get(id=id)
    obj,created=wishlist.objects.get_or_create(user=user)
    obj.products.add(product)
    obj.save()
    return redirect('home')

def addtocart(request,id):
    user=request.user
    product=watchupload.objects.get(id=id)
    obj,created=Cart.objects.get_or_create(user=user)
    obj.save()
    obj.products.add(product)
    obj.save()
    return redirect('home')

@login_required(login_url='login')
def show_wishlist(request):
    user=request.user
    wishlist_obj=wishlist.objects.get(user=user)
    return render(request, 'cart.html',{'product':wishlist_obj.products.all(),'iscart':False})

@login_required(login_url='login')
def show_cart(request):
    user=request.user
    cart_obj=Cart.objects.get(user=user)
    return render(request,'cart.html',{'product':cart_obj.products.all(),'iscart':True})

def remove_wish(request,id):
    product=watchupload.objects.get(id=id)
    wishlist_obj=wishlist.objects.get(user=request.user)
    wishlist_obj.products.remove(product)
    return render(request, 'cart.html',{'product':wishlist_obj.products.all(),'iscart':False})


def removecart(request,id):
    product=watchupload.objects.get(id=id)
    cart_obj=Cart.objects.get(user=request.user)
    cart_obj.products.remove(product)
    return render(request,'cart.html',{'product':cart_obj.products.all(),'iscart':True})

