"""allAuth001 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView
from social_app.views import verified_users_only_view, not_logged_view
from RestServiceEsse3.views import testRest, studentematricola, studentecodicefiscale, studenteemail, utentematricola, \
    utentecodicefiscale, utenteemail

from RestServiceScopus.views import scopusrequestbydoi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # <--
    path('', TemplateView.as_view(template_name="social_app/index.html")),  # <--
    path('altrapagina/', verified_users_only_view),  # <--
    path('paginanonloggata/', not_logged_view),  # <--

    #Metodi per richiamare rest service esse3
    path('restserviceesse3/testrest', testRest, name="testrest"),  # <--
    path('restserviceesse3/studentematricola/<str:matricola>/', studentematricola, name="studentematricola"),  # <--
    path('restserviceesse3/studentecodicefiscale/<str:codicefiscale>/', studentecodicefiscale, name="studentecodicefiscale"),  # <--
    path('restserviceesse3/studenteemail/<str:email>/', studenteemail, name="studenteemail"),  # <--
    path('restserviceesse3/utentematricola/<str:matricola>/', utentematricola, name="utentematricola"),  # <--
    path('restserviceesse3/utentecodicefiscale/<str:codicefiscale>/', utentecodicefiscale, name="utentecodicefiscale"),  # <--
    path('restserviceesse3/utenteemail/<str:email>/', utenteemail, name="utenteemail"),  # <--

    #Metodi per richiamare rest scopus
    path('restservicescopus/scopusrequestbydoi/<path:doi>/', scopusrequestbydoi, name="scopusrequestbydoi"),  # <--




]
