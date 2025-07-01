from .views import *
from django.urls import path

urlpatterns = [
    path('', index , name='main'),
    
    path('create/',addRecipe ,name='addRecipe'),
    path('delete_recipe/<slug:slug>/', delete_recipe , name='delete_recipe'),
    path('delete/<slug:slug>/', deleteVeiw , name='delete'),
    path('update_recipe/<slug:slug>/', update_recipe , name='update_recipe'),
    path('login/',login_page,name='login_page'),
    path('register/',register,name='register'),
    path('logout/',logout_page,name='logout'),
    path('want_logout', logoutView, name='logoutView'),
    path('details/<slug:slug>', detailsView , name='details')

]
