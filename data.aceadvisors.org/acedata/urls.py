"""acedata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

admin.site.site_header = "ACE Administration"
admin.site.site_title = "ACE Administration"
admin.site.index_title = "ACE Advisors"
urlpatterns = [
    # Other URL patterns
    


    path('admin/', admin.site.urls),
    path('api/', include('data.urls')),
    path('overview/', include('regulatory_overview.urls')),
    path('lifecycle', include('Investment_Lifecycle.urls')),
   
    
]

handler404 = 'data.views.error_404'

if settings.DEBUG:
    # Serve uploaded media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
