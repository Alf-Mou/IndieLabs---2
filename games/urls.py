from django.urls import path
from games.views import index

urlpatterns = [
    path('', index)
] 
