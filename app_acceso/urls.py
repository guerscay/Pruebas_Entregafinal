from django.urls import path
from app_acceso import views
from django.contrib.auth.views import LogoutView

app_name = 'app_acceso'

urlpatterns = [
    path ('login/', views.acceso_login, name = 'acceso_login'),
    path ('logout/', LogoutView.as_view(template_name = 'app_acceso/acceso_logout.html'), name = 'acceso_logout'),
    path ('registro/', views.acceso_registro, name = 'acceso_registro'),
    path('perfil', views.acceso_perfil, name = 'acceso_perfil' ),
    path('perfil/editar', views.acceso_perfil_editar, name = 'acceso_perfil_editar' )

]
