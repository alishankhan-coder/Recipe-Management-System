from django.shortcuts import render ,redirect
from django.http import JsonResponse
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
import random




# Create your views here.
lg_url = 'login/?next=/add_recipe/'
@login_required(login_url="/login")
def addRecipe(request):
    
    if request.method== "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_disc = data.get('recipe_desc')
        recipe_img = request.FILES['recipe_img']
        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_disc = recipe_disc,
            recipe_img = recipe_img,
            user = request.user,
            recipe_view_count = random.randint(10,50)
        )
        recp = f'{recipe_name} Created Successfully'
        messages.success(request,recp)
        return redirect('main')
    
    return render(request, 'update_recipe.html')






def index(request):
    query = request.GET.get('search', '')
    if query:
        recipes = Recipe.objects.filter(recipe_name__icontains=query)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'index.html' , {'recipes':recipes,'query':query})




def detailsView(request , slug):
    slg = slug
    recipes = Recipe.objects.filter(slug = slug)
    
    return render(request , 'details.html', {'recipes': recipes,'slg':slg})



@login_required(login_url='login')
def update_recipe(request,slug):
    recipe = Recipe.objects.get(slug = slug)
    if request.method == 'POST':
        data = request.POST
        name = data.get('recipe_name')
        disc = data.get('recipe_desc')
        
        recipe.recipe_name = name
        recipe.recipe_disc = disc
        if 'recipe_img' in request.FILES:
            recipe.recipe_img = request.FILES['recipe_img']
            
            
        recipe.save()
        messages.success(request , f'{recipe.recipe_name} Updated Successfully!')
        return redirect('main')
    
    return render(request, 'update_recipe.html', {'recipe': recipe})



def deleteVeiw(request, slug):
    recipes = Recipe.objects.filter(slug = slug)
    
    return render(request , 'delete.html',{'recipes': recipes, 'slg':slug})



@login_required
def delete_recipe(request, slug):
    if request.method ==  "POST":
        query = Recipe.objects.get(slug = slug)
        print(id)
        q = query.recipe_name
        query.delete()
        
        messages.success(request,f'{q} deleted Successfully!')
        return redirect('main')
    # return render(request,'delete.html')



def logoutView(request):
    return render(request,'logout.html')



def logout_page(request):
    if request.method ==  'POST':
            
        messages.error(request,'You are Logged Out. To create Recipes please Login Back')
        logout(request)
        return redirect('main')
    
    return render(request,'index.html')



def login_page(request):

    if request.method== "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username = username).exists():
            messages.error(request,'Username does not Exists!!!')
            return redirect('/login/')

        user = authenticate(request,username= username,password=password)
        print(user)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')

        login(request, user)
        messages.success(request,'Login Success.')
        return redirect('main')        


    return render(request, 'login.html')



def register(request):

    if request.method=='POST':
        username = request.POST.get('username')
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'UserName already Exists!!!')
            return redirect('/register/')

        user = User.objects.create(
            first_name= f_name,
            last_name= l_name,
            username = username
        )
        user.set_password(password)
        user.save()
        login(request,user)
        messages.success(request,'Account Created Successfully')
        return redirect('main')

    return render(request,'register.html')