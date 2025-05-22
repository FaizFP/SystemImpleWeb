
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard.html', views.dashboard_view, name='dashboard'),
    path('catatanpemeliharaan/', views.catatanpemeliharaan, name='catatanpemeliharaan'),
    path('simpan_project/', views.simpan_project, name='simpan_project'),
    path('project/form/', views.project_form_view, name='project_form'),
]