from django.urls import path, include
from . import views

urlpatterns = [
       path('', views.course_list, name='course_list'),
       path('<int:course_pk>/<int:step_pk>/', views.step_detail),
       path('suggest/', views.suggestion_view, name='suggestion'),
       path('<int:pk>/', views.course_detail,),
       
]