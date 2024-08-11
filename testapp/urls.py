from django.urls import path 
from . import views 

urlpatterns = [
    path('std/',views.employee_view)
]
