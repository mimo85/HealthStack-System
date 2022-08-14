from unicodedata import name
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', views.payment_home, name='payment_home'),
    path('ssl-payment-request/<int:pk>/<int:id>/', views.ssl_payment_request,
         name='ssl-payment-request'),
    path('ssl-payment-success/', views.ssl_payment_success,
         name='ssl-payment-success'),
    path('ssl-payment-fail/', views.ssl_payment_fail, name='ssl-payment-fail'),
    path('ssl-payment-cancel/', views.ssl_payment_cancel,
         name='ssl-payment-cancel'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)