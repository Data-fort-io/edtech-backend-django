from django.db import models

from django.db import models
from uuid import uuid4
from django.utils import timezone


# Tutor model
class Tutor(models.Model):
    """Model representing a tutor."""
    pass


# Enrollments (for managing students under tutors' courses)
class Enrollment(models.Model):
    """Model representing a student's enrollment."""
    pass

# Course model
class Course(models.Model):
    """Model representing an educational course."""
    pass

# Resource model
class Resource(models.Model):
    """Model for resources provided by tutors."""
    pass


# Recording model
class Recording(models.Model):
    """Model for class recordings submitted by tutors."""
    pass


# Notification model
class Notification(models.Model):
    """Model for notifications created by tutors."""
    pass


# Assessment model
class Assessment(models.Model):
    """Model for assessments created by tutors."""
    pass

# Submission + Grading model (optional: grade as its own model or inside submission)
class Submission(models.Model):
    """Model for student assessment submissions."""
    pass