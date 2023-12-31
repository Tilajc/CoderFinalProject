"""
URL configuration for coder_final_project project.

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

from app.views import home, about, CreatePost, Posts, UpdatePost, DeletePost, PostDetail, CreateComment, DeleteComment

urlpatterns = [
    path('home/', home, name="Home"),
    path('about/', about, name="About"),
    path('posts/', Posts.as_view(), name="Posts"),
    path('post/<int:pk>', PostDetail.as_view(), name="PostDetail"),
    path('create_post/', CreatePost.as_view(), name="CreatePost"),
    path('update_post/<int:pk>', UpdatePost.as_view(), name="UpdatePost"),
    path('delete_post/<int:pk>', DeletePost.as_view(), name="DeletePost"),
    path('create_comment/<int:pk>', CreateComment.as_view(), name="CreateComment"),
    path('delete_comment/<int:pk>', DeleteComment.as_view(), name="DeleteComment")
]
