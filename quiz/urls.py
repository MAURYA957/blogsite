import view as view
from . import views
from django.contrib import admin
from django.urls import path
from quiz.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addQuestion/', addQuestion, name='addQuestion'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),
    path('index/', index, name='index'),
    path('main/', main, name='main'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
