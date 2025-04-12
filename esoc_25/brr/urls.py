from django.urls import path
from .views import home,page3
urlpatterns = [
    path('', home, name='home'),
    path('page3/', page3, name='page3'),

]