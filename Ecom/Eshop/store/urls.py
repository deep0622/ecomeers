from django.urls import path
from .views import index , Signup




urlpatterns = [
        path('', index, name='homepage'),
        path('Signup', Signup)


]
