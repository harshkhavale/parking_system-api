from django.urls import path
from .views import RegisterView, LoginView, CheckInView, CheckOutView, ActiveVehiclesView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('checkin/', CheckInView.as_view(), name='checkin'),
    path('checkout/', CheckOutView.as_view(), name='checkout'),
    path('active-vehicles/', ActiveVehiclesView.as_view(), name='active-vehicles'),
]