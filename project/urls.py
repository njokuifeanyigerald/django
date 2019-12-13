from django.urls import path
from project.views import render_initial_data, project_detail_view
app_name = 'project'
urlpatterns = [

    path('r/<int:id>/', render_initial_data, name="render_data"),
    path('project/', project_detail_view, name = "render_data"),
]
