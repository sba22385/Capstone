from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})
