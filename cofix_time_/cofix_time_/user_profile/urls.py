from django.urls import path
from . import views

urlpatterns = [
    path('user_profile/', views.user_profile, name="user_profile"),
    path('time_abilities/', views.time_abilities, name="time_abilities"),
    path('stuff/', views.stuff, name="stuff"),
    path('schedule/', views.schedule, name="schedule"),
    path('cafes/', views.cafes, name="cafes"),
    path('schedule_making/', views.schedule_making, name="schedule_making"),
]
