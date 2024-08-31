from django.urls import include, path
from . import views


urlpatterns=[
  path('', views.login_view , name='login'),
  path('signup/', views.signup, name='signup'),
  path('forgot-password/', views.forgot_password, name='forgot-password'),

  

]