from django.contrib import admin
from django.urls import path, include
from appointments import views as appointments_views
from accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
    path('accounts/', include('accounts.urls')),
    path('predictor/', include('predictor.urls')),
    path('login/', accounts_views.user_login, name='login'),  # ← ADD THIS
]