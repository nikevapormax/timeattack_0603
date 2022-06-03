from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.category_view, name="category"),
]
