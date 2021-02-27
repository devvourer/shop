from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.create_user, name='create_user'),
    path('signup/verify/', views.verify, name='verify'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/', views.edit, name='edit')
]