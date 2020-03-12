from django.urls import path
from traveleverywhere import views

app_name = "traveleverywhere"

urlpatterns = [
    path('', views.home, name = "home"),
    path('blogs/', views.blogs, name = "blogs"),
    path('forum/', views.forum, name = "forum"),
    path('travel/', views.travel, name = "travel"),
	path('signup/', views.signup, name = "signup"),
	path('login/', views.login, name = "login"),
]