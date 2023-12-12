from django.urls import path
from .views import ModalListApiView, ModalDetailApiView


urlpatterns = [
    path('', ModalListApiView.as_view()),
    path('<int:pk>/', ModalDetailApiView.as_view()),
]