from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from login import views as login_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('login.urls'), name='home'),
    path('', include('dashboard.urls'), name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', login_views.logout_view, name='logout'),
    path('create_account/', login_views.create_account, name='create_account'),
    path('profile/', login_views.profile, name='profile'),
    path('admin/', admin.site.urls),
]

#Allows media to be accessed in debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)