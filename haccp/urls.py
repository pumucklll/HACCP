from django.urls import path
from . import views

urlpatterns = [
    path("", views.AllToDos.as_view(), name="index"),
    path("today/", views.TodayToDos.as_view(), name="today"),
    # import export
    path('home/', views.home, name='csv/home'),

    path('export-query-to-csv/', views.export_query_to_csv, name='cvs/export_query_to_csv'),

    path('import-csv/', views.import_csv, name='cvs/import_csv'),
]

#/admin/haccp/todoitem/add/