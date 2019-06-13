from django.urls import include, path

from logs.views import logs, admins, guests

urlpatterns = [
    path('', include('logs.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', logs.SignUpView.as_view(), name='signup'),
    path('accounts/signup/admin/', admins.AdminSignUpView.as_view(), name='admin_signup'),
    path('accounts/signup/guest/', guests.GuestSignUpView.as_view(), name='guest_signup'),
]
