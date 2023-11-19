from django.urls import path

from . import views

app_name = 'incidencias'

urlpatterns = [
    path('listado/', views.ListadoView.as_view(), name='listado'),
    path('incidencia/<int:pk>', views.CrearIncidenciaView.as_view(), name='crear'),
    path('incidencia/<int:pk>/guardar', views.guardar, name='guardar')
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
] 