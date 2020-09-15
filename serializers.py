from rest_framework import serializers
from.models import MontgomeryXRayMetadataReader

class MontgomeryXRayMetadataReaderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MontgomeryXRayMetadataReader
        fields = '__all__'