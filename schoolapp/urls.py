from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('continue/', views.new_page, name='new_page'),
    path('forms/',views.form_page,name='form_page'),
    path('logout',views.logout,name='logout')

]

