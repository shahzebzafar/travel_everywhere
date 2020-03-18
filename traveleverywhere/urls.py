from django.urls import path
from traveleverywhere import views

app_name = "traveleverywhere"

urlpatterns = [
    path('', views.home, name = "home"),
    path('blogs/', views.blogs, name = "blogs"),
    path('forum/', views.forum, name = "forum"),
    path('travel/', views.travel, name = "travel"),
	path('signup/', views.signup, name = "signup"),
	path('login/', views.user_login, name = "login"),
    path('logout/', views.user_logout, name='logout'),
    path('forum/<slug:question_name_slug>/', views.show_question, name = 'show_question'),
]