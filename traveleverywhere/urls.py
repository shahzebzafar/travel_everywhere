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
    path('forum/add_question/', views.add_question, name='add_question'),
    path('forum/show_question/<slug:question_name_slug>/', views.show_question, name = 'show_question'),
    path('forum/show_question/<slug:question_name_slug>/add_answer/', views.add_answer, name="add_answer"),
    path('blogs/add_blog/', views.add_blog, name = 'add_blog'),
    path('blogs/<slug:blog_name_slug>/', views.show_blog, name = 'show_blog'),
]