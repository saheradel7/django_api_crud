from django.urls import path
from .views import EmployeeDetail


urlpatterns = [
    path("crud" , EmployeeDetail.as_view(), name= "emp")
]