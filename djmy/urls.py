from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

def home(request):
    return HttpResponse("<h1>Xoş gelmisiz! Polls app-e keçin : <a href='/polls/'>/polls/</a></h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', home, name='home'),  # Ana səhifə
]