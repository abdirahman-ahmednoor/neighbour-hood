from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
  path('', views.index, name="index"),
  path('register/', views.register, name="register"),
  path('accounts/login/',views.login,name='login'),
  path('accounts/profile/',views.profile,name='profile'),
  path('update/',views.update_profile,name='update_profile'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'django_registration/logout.html'),name='logout'),
  path('search/',views.search,name='search'),
  path('neighborhood/<int:neighborhood_id>/',views.neighborhood,name='neighborhood'),
  path('create_neighborhood/',views.create_neighborhood,name='create_neighborhood'),
  path('create_business/<int:neighborhood_id>/',views.create_business,name='create_business'),
  path('choose_neighborhood/<int:neighborhood_id>/',views.choose_neighborhood,name='choose_neighborhood'),
  path('leave_neighborhood/<int:neighborhood_id>/',views.leave_neighborhood,name='leave_neighborhood'),
  path('create_post/<int:neighborhood_id>/',views.create_post,name='create_post'),
  path('delete_business/<business_id>',views.delete_business,name='delete_business'),
  path('update_business/<business_id>',views.update_business,name='update_business'),
  path('delete_post/<post_id>',views.delete_post,name='delete_post'),
  path('update_post/<post_id>',views.update_post,name='update_post'),
  path('update_neighborhood/<neighborhood_id>',views.update_neighborhood,name='update_neighborhood'),
  path('delete_neighborhood/<neighborhood_id>',views.delete_neighborhood,name='delete_neighborhood'),
  path('users/<pk>',views.users_profile,name='users_profile'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
