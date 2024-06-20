from django.urls import path
from .views import home, get_plan

urlpatterns = [
    path('home/', home, name='home'),
    path('consult/', get_plan, name='consult'),
]
