from django.db import models
from django.contrib.auth.models import AbstractUser


class StudentProfile(AbstractUser):
    USER_ROLE = [
        ('student', 'Student'),
        ('lecturer', 'Lecturer'),
        ('prof', 'Professor'),
    ]

    student_id = models.CharField(max_length=7, unique=True, null=False)
    role = models.CharField(max_length=10, choices=USER_ROLE, default='student')
    department = models.CharField(max_length=20)
    address = models.CharField(max_length=50, blank=True)
    emergency_contact = models.CharField(max_length=15, blank=True)
    bio = models.TextField(blank=True)
    started_at = models.DateTimeField()
    expected_to_graduate = models.DateTimeField()

    class Meta:
        verbose_name = "Student Profile"
        verbose_name_plural = "Student Profiles"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"


class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credit_hour = models.PositiveIntegerField()
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.title}"


class Enrollment(models.Model):
    STATUS = [
        ('active', 'Active'),
        ('dropped', 'Dropped'),
        ('completed', 'Completed'),
        ('not_enrolled', 'Not Enrolled'),
    ]

    student = models.ForeignKey(StudentProfile, related_name='enrollments', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS, default='not_enrolled')

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.username} → {self.course.code} ({self.status})"
