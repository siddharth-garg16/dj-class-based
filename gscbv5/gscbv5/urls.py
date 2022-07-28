"""gscbv5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TemplateView.as_view(template_name="school/home.html"), name="blankhome"),
    path('home/', views.RedirectView.as_view(url="/"), name="home"),
    path('index/', views.RedirectView.as_view(pattern_name="home"), name="index"),#pattern name should match thhe name in the other path field
    # path('google/', views.RedirectView.as_view(url="https://www.google.com"), name="google"),#external link
    path('ggl/', views.GoogleRedirectView.as_view(), name="google2"),
    path('ig/', views.RedirectView.as_view(url="https://www.reddit.com"), name="reddit"), #higher preference for ig since written earlier
    path('ig/', views.RedirectView.as_view(url="https://www.instagram.com"), name="ig"),
]
#if we have multiple redirect views to same url first written path will have higher preference