from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import Apartments, User
from django.contrib.auth.models import auth, User
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login



class IndexView(generic.ListView):
    template_name ="rent_website/home.html"
    context_object_name = "all_apartments"
    def get_queryset(self):
        return Apartments.objects.all()

def details(request, id):
    apartment = Apartments.objects.get(id = id)
    return render(request, 'rent_website/details.html', {'apartment': apartment})

class FavoriteView(generic.ListView):
    template_name = "rent_website/favorites.html"
    def get_queryset(self):
        if Apartments.favorite == True:
            return Apartments.object.all()


def register(request):
    #form = UserCreationForm()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password == password_confirmation:
            if User.objects.filter(username = username).exists():
               messages.info(request, "Username taken")
            elif User.objects.filter(email = email).exists():
               messages.info(request, "Email taken")
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, username = username, password = password,)
                user.save()
                print('user created')
                #return redirect("/login")
                return render(request, 'rent_website/login.html')

    else:
        return render(request, 'rent_website/register.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "User does not exist")
            return redirect("/login")
    else:

        return render(request, "rent_website/login.html")



def logout(request):
    auth.logout(request)
    return redirect("/")

def search(request):
    return render(request, 'rent_website/search.html')

