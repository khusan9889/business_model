from rest_framework import generics
from .models import Modal
from .serializers import ModalSerializer


class ModalListApiView(generics.ListCreateAPIView):
    queryset = Modal.objects.all()
    serializer_class = ModalSerializer

class ModalDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modal.objects.all()
    serializer_class = ModalSerializer
