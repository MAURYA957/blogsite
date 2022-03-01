from . import views
from django.urls import path
from .views import about, Contact
from .feeds import LatestPostsFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path(' ', about, name='about'),
    path("feed/rss", LatestPostsFeed(), name='post_feed'),
    path('admin/upload', views.image_upload_view, name='upload_view'),
    path('<slug:slug>/', Contact, name='Contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
