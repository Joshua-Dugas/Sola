from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from login import views as login_views


urlpatterns = [
    path('', include('login.urls'), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', login_views.logout_view, name='logout'),
    path('create_account/', login_views.create_account, name='create_account'),
    path('admin/', admin.site.urls),
]