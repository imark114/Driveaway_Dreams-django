from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(),name='login'),
    path('logout/', views.UserLogoutView.as_view(),name='logout'),
    path('profile/', views.profile,name='profile'),
    path('update_profile/',views.edit_profile, name='update_profile'),
    path('change_password/',views.PassChangeView.as_view(),name='pass_change')
]
