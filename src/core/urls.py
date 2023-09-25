from django.urls import path

from core.views import IndexView
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('collections/', views.list_csv_files, name='collections'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('display_csv/<str:file_name>/', views.display_csv_content, name='display_csv_content'),
]
