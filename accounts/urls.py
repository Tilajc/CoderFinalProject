from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import signup, login_request, update, profile, delete_user, update_avatar

urlpatterns = [
    path("signup/", signup, name="Signup"),
    path("update/", update, name="Update"),
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
    path('profile/', profile, name="Profile"),
    path('delete/', delete_user, name="Delete"),
    path('avatar/', update_avatar, name="UpdateAvatar")
]
