from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import UserProfile,Post,Neighborhood,Business,Comment
from django.contrib.auth.decorators import login_required
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .serializer import BusinessSerializer
from .email import send_amber_email
from .forms import *
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