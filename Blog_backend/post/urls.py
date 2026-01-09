from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.postOverview, name="post_overview"),
    path('api/posts/get', views.viewAllPost, name="view_all_post"),
    path('api/posts/add', views.addPost, name="add_post"),
    path('api/posts/get/<int:pk>', views.viewPost, name="get_post"),
    path('api/posts/get/<int:pk>/update', views.updatePost, name="update_post"),
    path('api/posts/get/<int:pk>/delete', views.deletePost, name="delete_post"),
    path('api/posts/get/<int:pk>/like', views.likePost, name="like_post"),
    path('api/posts/get/<int:post_id>/comment/get', views.viewAllComment, name="get_comment"),
    path('api/posts/get/<int:post_id>/comment/add', views.addComment, name="add_comment"),
    path('api/posts/get/<int:post_id>/comment/get/<int:pk>/update', views.updateComment, name="update_comment"),
    path('api/posts/get/<int:post_id>/comment/get/<int:pk>/delete', views.deleteComment, name="delete_comment"),
    path('api/posts/get/<int:post_id>/comment/get/<int:pk>/like', views.likeComment, name="like_comment"),
]