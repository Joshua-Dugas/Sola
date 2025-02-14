from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('login/', include('login.urls')),
    path('login/create_account/', include('login.urls')),
    path('admin/', admin.site.urls),
]