from rest_framework import serializers
from .models import Modal
from control.serializers import ControlSerializer
from input.serializers import InputSerializer
from mechanism.serializers import MechanismSerializer
from output.serializers import OutputSerializer
from control.models import Control
from input.models import Input
from mechanism.models import Mechanism
from output.models import Output


class ModalSerializer(serializers.ModelSerializer):
    control = ControlSerializer(required=False, many=True)
    output = OutputSerializer(required=False, many=True)
    mechanism = MechanismSerializer(required=False, many=True)
    input = InputSerializer(required=False, many=True)

    class Meta:
        model = Modal
        fields = ('id', 'name', 'control', 'output', 'mechanism', 'input')

    def create(self, validated_data):
        control_data = validated_data.pop('control', [])
        output_data = validated_data.pop('output', [])
        mechanism_data = validated_data.pop('mechanism', [])
        input_data = validated_data.pop('input', [])

        # Create Modal instance
        modal = Modal.objects.create(name=validated_data.get('name'))

        # Update model_id for Input, Output, Mechanism, and Control instances
        for data_list, model_class in zip([input_data, output_data, mechanism_data, control_data], [Input, Output, Mechanism, Control]):
            for data in data_list:
                data['model_id'] = modal

        # Create Input, Output, Mechanism, and Control instances if data is provided
        input_instances = Input.objects.bulk_create([Input(**data) for data in input_data])
        output_instances = Output.objects.bulk_create([Output(**data) for data in output_data])
        mechanism_instances = Mechanism.objects.bulk_create([Mechanism(**data) for data in mechanism_data])
        control_instances = Control.objects.bulk_create([Control(**data) for data in control_data])

        modal.save()

        return modal
