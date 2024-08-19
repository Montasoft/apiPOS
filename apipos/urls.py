
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compras/', include('apps.compras.urls')),
    path('baseapp/', include('apps.baseapp.urls')),
    path('inventario/', include('apps.inventario.urls')),
    path('', include('apps.compras.urls')),
]
