from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.views.generic import TemplateView


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]