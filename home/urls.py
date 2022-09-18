from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('api/get-quiz/', views.get_quiz, name="get-quiz")
]
