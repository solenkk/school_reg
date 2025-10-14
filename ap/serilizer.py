from rest_framework import serializers
from .models import StudentProfile, Course, Enrollment

class StudentProfileserializer(serializers.ModelSerializer):
    model= StudentProfile
    class Meta:
        fields= ('student_id','id','department','fristname','lastname')

class Courseserilserializer(serializers.Modelserializer):
    model=Course
    class Meta:
        student_identity=StudentProfileserializer(source='StudentProfile' , read_only=True)

        feild=('title','code', 'credit_hour', 'instructor','id')

class EnrollmentSerialzer(serializers.Modelserializer):
    model=Enrollment
    stuedent_identity= StudentProfileserializer(source='studentprofile', read_only=True)
    class Meta:
    
        fields=('date_enrolled','student','course','id')