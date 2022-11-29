from django.contrib import admin
from django.urls import path
from .views import about,index,signup,signin,product,cart,signout,add_to_cart,remove_from_cart,search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="home"),
    path('signup/', signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('product/',product,name='product'),
    path('about/',about,name='about'),
    path('cart/',cart,name='cart'),
    path('addtocart/',add_to_cart,name='addtocart'),
    path('addtocart/<int:id>',add_to_cart, name= 'addtocart'),
    path("removefromcart",remove_from_cart, name="removefromcart"),
    path("removefromcart/<int:id>",remove_from_cart, name="removefromcart"),
    path('signout/',signout,name='signout'),
    path('search/',search,name='search'),
    
]

