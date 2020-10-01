
from django.urls import path


from website import views

urlpatterns = [
    path('', views.index),
    path('contacts/', views.contacts),
    path('publications/', views.publications),
    path('publications/<int:pk>/', views.publication),
    path('publish', views.publish),
    path('about', views.about),

]
