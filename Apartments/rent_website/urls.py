from django.urls import path
from . import views

app_name = "rent_website"

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path("<int:id>", views.details, name = 'details'),
    path("favorites", views.FavoriteView.as_view(), name = 'details'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('search', views.search, name = 'search'),
    path('logout', views.logout, name='logout')



]
