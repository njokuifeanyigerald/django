

from django.urls import path
from class_app.views import ClassListView, ClassDetailView, ClassCreateView, ClassUpdateView, ClassDeleteView
app_name = "class_app"
urlpatterns = [
    path('', ClassListView.as_view(), name="class_list_view"),
    path('create/', ClassCreateView.as_view(), name="class_create_view"),
    path('<int:pk>/', ClassDetailView.as_view(), name="class_detail"),
    path('<int:pk>/update/', ClassUpdateView.as_view(), name="class_update"),
    path('<int:pk>/delete', ClassDeleteView.as_view(), name="class_delete"),

]
