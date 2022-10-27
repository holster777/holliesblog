from django.conf import settings
from django.urls import include, path
from django.contrib import admin    

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from . import views

urlpatterns = [
   path('login_user', views.login_user, name='login'),
   path('logout_user', views.logout_user, name='logout'),
   path('register_user', views.register_user, name='register'),
]

