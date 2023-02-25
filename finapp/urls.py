from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),

    path("customer_registration/", views.customer_registration, name="customer_registration"),
    path("freelancer_registration/", views.freelancer_registration, name="freelancer_registration"),

    path("customer_login/", views.customer_login, name="customer_login"),
    path("freelancer_login/",views.freelancer_login,name="freelancer_login"),

    path("change_password/", views.change_password, name="change_password"),
    path("logout/", views.Logout, name="logout"),
    
    path('job/<int:pk>/', views.job_details, name="job_details" ),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
