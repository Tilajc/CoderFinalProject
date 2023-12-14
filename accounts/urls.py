from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import signup, login_request, update, users, profile

urlpatterns = [
    path("signup/", signup, name="Signup"),
    path("update/", update, name="Update"),
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="Logout"),
    path('users/', users, name="Users"),
    path('profile/', profile, name="Profile"),
]
