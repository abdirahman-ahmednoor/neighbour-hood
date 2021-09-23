from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http  import HttpResponse

# Create your views here.
@login_required
def index(request):
    current_user = request.user
    try:
        profile = UserProfile.objects.get(user =current_user)
    except:
        return redirect('edit_profile', username = current_user.username)

    try:
        post = Post.objects    