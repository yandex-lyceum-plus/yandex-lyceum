from django.urls import path
from users import views


urlpatterns = [
    path('signup/', views.SignupPage.as_view(), name='signup'),

    path('profile/', views.ProfilePage.as_view(), name='profile'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('users/', views.UserList.as_view(), name='user_list'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
