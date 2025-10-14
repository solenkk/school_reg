from rest_framework import serializers
from .models import StudentProfile, Course

class StudentProfileserializer(serializers.ModelSerializer):
    class Meta:
        model= StudentProfile
        fields= ('student_id','id','department','fristname','lastname')
class Courseserilserializer(serializers.Modelserializer):
    class Meta:
        
        feild