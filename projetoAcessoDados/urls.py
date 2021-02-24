from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('dados/', include('acessoDados.urls')),
    path('admin/', admin.site.urls),
]
