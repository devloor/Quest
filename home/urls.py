from django.urls import path
from .views import hello_view, student, newstud

urlpatterns = [
      path('', hello_view, name="home"),
      path('student/', student),
      path("newstudent/", newstud, name="Register"),
]