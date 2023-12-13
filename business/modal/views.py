from rest_framework import generics
from .models import Modal
from .serializers import ModalSerializer, ModalDetailWithRelatedDataSerializer
from rest_framework.response import Response
from control.serializers import ControlSerializer
from input.serializers import InputSerializer
from mechanism.serializers import MechanismSerializer
from output.serializers import OutputSerializer


class ModalListApiView(generics.ListCreateAPIView):
    queryset = Modal.objects.all()
    serializer_class = ModalSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        modals_with_related_data = []
        for modal_instance in queryset:
            related_data = {
                'controls': ControlSerializer(modal_instance.control_set.all(), many=True).data,
                'inputs': InputSerializer(modal_instance.input_set.all(), many=True).data,
                'mechanisms': MechanismSerializer(modal_instance.mechanism_set.all(), many=True).data,
                'outputs': OutputSerializer(modal_instance.output_set.all(), many=True).data,
            }
            modal_data = ModalSerializer(modal_instance).data
            modal_data['related_data'] = related_data
            modals_with_related_data.append(modal_data)

        return Response(modals_with_related_data)

class ModalDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Modal.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ModalDetailWithRelatedDataSerializer
        return ModalSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        related_data = {
            'controls': ControlSerializer(instance.control_set.all(), many=True).data,
            'inputs': InputSerializer(instance.input_set.all(), many=True).data,
            'mechanisms': MechanismSerializer(instance.mechanism_set.all(), many=True).data,
            'outputs': OutputSerializer(instance.output_set.all(), many=True).data,
        }

        data = serializer.data
        data['related_data'] = related_data

        return Response(data)