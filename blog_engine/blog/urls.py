from django.urls import path

from .views import blog_list, tag_list
from .views import PostDetail, PostCreate, PostUpdate, PostDelete
from .views import TagDetail, TagCreate, TagUpdate, TagDelete


urlpatterns = [
    # urlpatterns post
    path('', blog_list, name='post_list_url'),
    path('post/create/', PostCreate.as_view(), name = 'post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    # urlpatterns tag
    path('tags/', tag_list, name='tag_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url' ),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url')
]
