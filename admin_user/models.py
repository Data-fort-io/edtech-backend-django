from django.db import models
from uuid import uuid4
from django.db import models
from django.utils import timezone
from dataforte.models import CourseSchema, EnrollmentSchema, ResourceSchema, RecordingSchema, NotificationSchema

class Course(models.Model):
    """Model representing an educational course."""
    pass
   


class Enrollment(models.Model):
    """Model representing a student's enrollment in a course."""

    ENROLLMENT_STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    pass


class Resource(models.Model):
    """Model for learning resources attached to a course."""
    pass


class Recording(models.Model):
    """Model for storing class recording links."""
    pass


class Notification(models.Model):
    """Model for user notifications."""
    pass
