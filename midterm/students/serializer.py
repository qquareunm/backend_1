from rest_framework import serializers
from .models import Student




class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(allow_null=False, allow_blank=False)
    surname = serializers.CharField(allow_null=False, allow_blank=False)
    year_of_study = serializers.IntegerField(allow_null=False)

    def create(self, validated_data):
        students = Student(**validated_data)
        students.save()
        return students


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance