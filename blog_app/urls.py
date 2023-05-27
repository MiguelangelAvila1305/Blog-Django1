from django.urls import path
from .views import BlogListView, BlogDetailView, CreatePost,UpdatePost, DeletePost

urlpatterns=[
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),
    path('create_post/', CreatePost.as_view(), name='create_post'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePost.as_view(), name='delete_post'),
    
]
