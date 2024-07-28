"""
cars/urls.py
"""

from django.urls import path
from .views import (
    CarListView,
    NewCarCreateView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView,
)

urlpatterns = [
    path("", CarListView.as_view(), name="cars_list"),
    path("search/", CarListView.as_view(), name="cars_search"),
    path("new/", NewCarCreateView.as_view(), name="cars_new"),
    path("detail/<uuid:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("update/<uuid:pk>/", CarUpdateView.as_view(), name="car_update"),
    path("delete/<uuid:pk>/", CarDeleteView.as_view(), name="car_delete"),
]
