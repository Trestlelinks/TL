from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.benchresource_form),
    path('list/',views.benchresource_list),    
    path('benchresource', views.benchresource),  
    path('benchshow',views.benchshowview),  
    path('benchedit/<int:id>', views.benchedit),  
    path('benchupdate/<int:id>', views.benchupdate),  
    path('benchdelete/<int:id>', views.benchdestroy),  
]
