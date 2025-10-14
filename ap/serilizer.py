from rest_framework import serializers
from .models import student_profile

class student_profileserilizer(serializers.ModelSerializer):
    class Meta:
        model= student_profile
        fields= ('student_id','id','department')