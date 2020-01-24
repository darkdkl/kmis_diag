from rest_framework import serializers
from .models import Diagnostics, Device, Result


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class DiagnosticsSerializer(serializers.ModelSerializer):

    device = DeviceSerializer()
    results = ResultSerializer(many=True)

    def create(self, validated_data):
        device_data = validated_data.pop('device')
        results_data = validated_data.pop('results')
        # raise Exception(results_data)
        device = Device.objects.create(**device_data)
        results = [Result.objects.create(**result) for result in results_data]
        diagnostics = Diagnostics.objects.create(device=device, **validated_data)
        diagnostics.results.set(results)
        return diagnostics

    class Meta:
        model = Diagnostics
        fields = ['name', 'date', 'device', 'description',
                  'conclusion', 'file', 'file_md5', 'results']
       