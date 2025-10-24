"""
URL configuration for bookListerProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from book_app.views import home
from book_app.views import allbooks
from book_app.views import addBook
from book_app.views import viewBook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('allbooks/', allbooks, name='allbooks'),
    path('add/', addBook, name='addBook'),
    path('viewbook/<int:book_id>/', viewBook, name='viewBook')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)