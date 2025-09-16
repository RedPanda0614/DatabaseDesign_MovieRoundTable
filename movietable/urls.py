"""
URL configuration for movietable project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import app01.views
from django.urls import path
import accounts.views

urlpatterns = [
    path('register/', accounts.views.register, name='register'),
    path('login/', accounts.views.user_login, name='login'),
    path('index/', accounts.views.search, name='search'),
    # path('search_movie/', app01.views.search_movie, name='search_movie'),
    path('search/', app01.views.search, name='search'),
    path('submit_review/', app01.views.submit_review, name='submit_review'),
    path('title_info/<str:title>/', app01.views.title_info, name='title_info'),
    path('administrator_register/', accounts.views.administrator_register, name='administrator_register'),  # 管理员注册
    path('administrator_login/', accounts.views.administrator_login, name='administrator_login'),  # 管理员登录
    path('administrator/', app01.views.administrator_show, name='administrator'),  # 管理员登录
    path('user/<int:user_id>/', accounts.views.user_profile, name='user_profile'),  # 用户主页
    path('update_user_info', accounts.views.update_user_info, name='update_user_info'),  # 用户修改信息
    path('mark/<int:user_id>', app01.views.get_mark, name='get_mark'),  # 获取标记（评论）信息
    path('delete_comment/<int:comment_id>/', app01.views.delete_comment, name='delete_comment'), # 删除标记
    path('delete_user/<int:user_id>/', app01.views.delete_user, name='delete_user') # 管理员删除用户

]
