from django.urls import path
from .views import NewsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete
from .views import upgrade_me

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
]