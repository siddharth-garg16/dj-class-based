from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#login required makes sure profile s accessible only when logged in
@login_required
def profile(request):
    return render(request, "registration/profile.html")