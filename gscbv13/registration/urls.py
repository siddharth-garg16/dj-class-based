from django.urls import path
from registration import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('profile/', login_required(views.ProfileView.as_view()), name="profile"),
]