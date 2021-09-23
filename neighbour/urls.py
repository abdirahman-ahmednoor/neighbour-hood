from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

from django_registration.backends.one_step.views import RegistrationView
urlpatherns= {
    path('', views.index, name= 'index'),
    path('^edit_profile/(?P<username>\w{0,50})',views.edit_profile,name = 'edit_profile'),
    path('businesses/',views.businesses,name = 'businesses'),
    path('post/(?P<id>\d+)',views.post,name='post'),
    path('search/',views.search,name='search'),
    # path('api/businesses/$',views.BusinessList.as_view()),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('^accounts/register/',RegistrationView.as_view(success_url='/accounts/login'),name='django_registration_register'),

}