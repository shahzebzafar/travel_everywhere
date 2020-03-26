from django.urls import path
from traveleverywhere import views
from traveleverywhere.views import MyAccountView

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
    path('blogs/show_blog/<slug:blog_name_slug>/', views.show_blog, name = 'show_blog'),
    path('blogs/show_blog/<slug:blog_name_slug>/add_image/', views.add_image, name="add_image"),
    path('my_account/<username>/', views.MyAccountView.as_view(), name='my_account'),
    path('like_blog/', views.LikeBLogView.as_view(), name = "like_blog" ),
    path('like/', views.LikeAirline.as_view(), name = "like" ),
]