from django.urls import path
from . import views

urlpatterns = [
    #path('', views.cardiology_prediction, name="cardiology_prediction"),
    path('', views.index, name = "index"),
    path('form/', views.CardioForm, name = "CardioForm"),
    path('result/', views.result, name = "result"),
    path('predict/',views.predict, name="predict"),
]

