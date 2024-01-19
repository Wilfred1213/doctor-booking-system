from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.index, name = 'index'),
    path('appointment/', views.appointment, name='appointment'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('department/', views.department, name='department'),
    path('department_detail/<int:department_id>/', views.department_detail, name='department_detail'),
    path('doctor/', views.doctor, name='doctor'),
    path('doctor_detail/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
    path('blog_detail/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('accept_appointment/<int:patient_id>/', views.accept_appointment, name='accept_appointment'),
    path('reject_appointment/<int:patient_id>/', views.reject_appointment, name='reject_appointment'),
    path('treated_appointment/<int:patient_id>/', views.treated_appointment, name='treated_appointment'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('category_detail/<int:cat_detail>/', views.category_detail, name='category_detail'),
    path('tags/<int:blog_id>/', views.tags, name='tags'),
] 