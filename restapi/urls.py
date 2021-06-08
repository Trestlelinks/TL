from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   path('api/employees', views.employeelist.as_view()),
]