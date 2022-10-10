
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('EngineHomePage/',include('SearchEngine.urls')),
    path('admin/', admin.site.urls),
]
