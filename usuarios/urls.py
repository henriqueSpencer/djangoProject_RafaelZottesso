from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
#    #path('endereço/', IndexView.as_view(), name='nome-da-url'),
    path('login', auth_views.LoginView.as_view(template_name='usuarios/form.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout')
]