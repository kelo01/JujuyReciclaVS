from django.contrib import admin
from django.urls import path
from core import views as core_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', core_views.LoginView.as_view(), name='login'),
    path('registro/', core_views.RegistroView.as_view(), name='registro'),
    path('logout/', core_views.LogoutView.as_view(), name='logout'),


    #Agente
    path('inicio/Agente/',core_views.inicio_agente, name='inicio_agente'),
    
    path('inicio/EcoUser/', core_views.inicio_agente, name='inicio_usuario'),
    


    path('admin/', admin.site.urls),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)