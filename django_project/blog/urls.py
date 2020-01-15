"""


"""

from django.urls import path
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
                    )

# structure here is 1. page 2. what module handles it 3. the name of the page
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), #home page
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # detail post, view class
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), # update view post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), # delete view post
    path('about/', views.about, name='blog-about'), #about page
    path('post/new/', PostCreateView.as_view(), name='post-create'), # Post creation
]

# <app>/<model>_<viewtype>.html