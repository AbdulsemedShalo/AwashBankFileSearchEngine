
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',include('SearchEngine.urls')),
    path('Discussion-Forum/', include('AwashForum.urls')),
    path('admin/', admin.site.urls),
]
