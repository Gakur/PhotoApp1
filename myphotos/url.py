from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index, name = 'index'),
    path('post/<id>', views.comment, name = 'comment'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('like', views.like, name='like_post'),
    path('search/', views.search_results, name='search'),
    path('upload/profile', views.upload_profile, name='upload_profile'),
    path('follow/<to_follow>', views.follow, name='follow'),
]

if settings.DEBUG:
	urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
