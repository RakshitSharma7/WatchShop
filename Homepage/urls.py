
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.Home,name='home'),
    path('about/',views.about ,name='about'),
    path('upload/',views.upload ,name='upload'),
    path('login/',views.login_page,name='login'),
    path('signup/',views.signup_page,name='signup'),
    path('logout/',views.logout_page,name='logout'),
    path('product/<int:id>',views.show_product,name='product'),
    path('addtowish/<int:id>',views.addtowish,name='wishlist'),
    path('addtocart/<int:id>',views.addtocart,name='cart'),
    path('wishlist',views.show_wishlist,name='show_wishlist'),
    path('cart',views.show_cart,name='show_cart'),
    path('removewish/<int:id>',views.remove_wish,name='removewish'),
    path('removecart/<int:id>',views.removecart,name='removecart')
]


urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)