from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('<int:customer_id>/', views.customer_detail, name='customer_detail'),
    path('camera/', views.camera_view, name='camera'),
    path('camera/upload/', views.camera_upload, name='camera_upload'),
]

