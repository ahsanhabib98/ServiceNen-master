from django.conf.urls import url
from .views import sign_up, profile, profile_details, edit_profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/', sign_up, name='signup'),
    url(r'^login/',auth_views.login,{'template_name': 'registration_app_html/login.html'},name='login'),
    url(r'^logout/',auth_views.logout,{'template_name': 'home.html'},name='logout'),
    url(r'^profile/', profile, name='profile'),
    url(r'^profile_details/', profile_details, name='profile_details'),
    url(r'^profile_edit/', edit_profile, name='edit_profile'),

]
