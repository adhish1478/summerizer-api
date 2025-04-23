from rest_framework import serializers

class SummarizeTextSerializer(serializers.Serializer):
    text= serializers.CharField(max_length=1000)

    def validate_text(self, value):
        if len(value)<10:
            raise serializers.ValidationError("Text is too short")
        return value