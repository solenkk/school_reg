from rest_framework import serializers
from .models import StudentProfile, Course, Enrollment


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ('id', 'student_id', 'department', 'first_name', 'last_name')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'code', 'credit_hour', 'instructor')


class EnrollmentSerializer(serializers.ModelSerializer):
    # Nested serializer (read-only)
    student_identity = StudentProfileSerializer(source='student', read_only=True)
    course_info = CourseSerializer(source='course', read_only=True)

    class Meta:
        model = Enrollment
        fields = ('id', 'student', 'course', 'date_enrolled', 'status', 'student_identity', 'course_info')
