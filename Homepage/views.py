from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import WatcheDB,watchupload,wishlist,Cart,Watchreviews,cartItems
from  . forms import uploadforms,contactform
from django.contrib.auth.decorators import login_required

# Create your views here.




def Home(request):
    watches = watchupload.objects.all()
    context={"watches_t":watches}
    return render(request, 'home.html', context)

# @login_required(login_url='login')
# def upload(request):
#     if request.method == "POST":
#         form = uploadforms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = uploadforms()

#     return render(request, "upload.html", {'form': form})



#class-based view
from django.views import View
from django.utils.decorators import method_decorator

class uploadPage(View):

    @method_decorator(login_required(login_url='login'))
    def get(self,request):
        form = uploadforms()
        return render(request, "upload.html", {'form': form})
    @method_decorator(login_required(login_url='login'))
    def post(self,request):
        form = uploadforms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
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

from django.contrib import messages

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect if the user is already logged in

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})



def logout_page(request):
    logout(request)
    return redirect('home')

from django.shortcuts import get_object_or_404
def show_product(request,id):
    product = get_object_or_404(watchupload,id=id)
    review_obj=Watchreviews.objects.filter(products=product)
    return render(request,'product.html',{'product':product,'reviews':review_obj})


def addtowish(request,id):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = request.user
        product = watchupload.objects.get(id=id)
        obj,created=wishlist.objects.get_or_create(user=user)
        obj.products.add(product)
        obj.save()
        return redirect('home')
    else:
        return redirect('login')

def addtocart(request,id):
    #check if user has cart or not
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    
    #fetch the product with given id
    product= watchupload.objects.get(id=id)

    #create a cart item using product abd user
    cart_item, created = cartItems.objects.get_or_create(user= user_cart, product=product)
    cart_item.product=product
    cart_item.save()
    return redirect('home')

@login_required(login_url='login')
def show_wishlist(request):
    user=request.user
    wishlist_obj=wishlist.objects.get(user=user)
    return render(request, 'wishlist.html',{'product':wishlist_obj.products.all(),'iscart':False})

@login_required(login_url='login')
def show_cart(request):
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_objects = user_cart.cartitems_set.all()
    return render(request, 'cart.html', {'product': cart_objects})

def remove_wish(request,id):
    product=watchupload.objects.get(id=id)
    wishlist_obj=wishlist.objects.get(user=request.user)
    wishlist_obj.products.remove(product)
    return render(request, 'wishlist.html',{'product':wishlist_obj.products.all(),'iscart':False})


# def removecart(request,id):
#     product_rm = watchupload.objects.get(id=id)
#     cart_user,created=Cart.objects.get_or_create(user=request.user)
#     cart_obj= cartItems.objects.filter(user=cart_user,product=product_rm)
#     cart_obj.product.remove(product_rm)
#     return render(request, 'cart.html', {'product': cart_obj.product.all()})

def removecart(request, id):
    product_rm = watchupload.objects.get(id=id)
    cart_user = Cart.objects.get(user=request.user)
    cart_item = cartItems.objects.get(user=cart_user, product=product_rm)
    cart_item.delete()
    return redirect('show_cart')


def contact(request):
    return render(request,'contact.html')


class contactus(View):

    @method_decorator(login_required(login_url='login'))
    def get(self,request):
        form = contactform()
        return render(request, "contact.html", {'form': form})
    @method_decorator(login_required(login_url='login'))
    def post(self,request):
        form = contactform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, "contact.html", {'form': form})
    
class SearchView(View):
    model = watchupload
    template_name = 'search.html'
    
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if query:
            results = watchupload.objects.filter(name__icontains=query).order_by('-updated')
        else:
            results = watchupload.objects.none()
        return render(request, self.template_name, {'get': results})
