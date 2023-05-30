"""
URL configuration for notebookIPZ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views as todo_views
from authentication import views as authentication_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page
    path('', authentication_views.home, name='home'),

    # Authentication
    path('signup/', authentication_views.signup_user, name='signup'),
    path('login/', authentication_views.login_user, name='login'),
    path('logout/', authentication_views.logout_user, name='logout'),

    # Todos
    path('weeklist/', todo_views.week_list, name='week_list'),
    path('week/<int:week_pk>', todo_views.week_show, name='week_show'),
    path('week/create_todo', todo_views.create_todo, name='create_todo'),
    path('week/delete_todo', todo_views.delete_todo, name='delete_todo'),
]
