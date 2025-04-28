from pydantic import BaseModel, EmailStr
from typing import List, Optional
from uuid import UUID
from datetime import datetime



class CourseSchema(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    created_by: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime


class EnrollmentSchema(BaseModel):
    id: UUID
    user_id: UUID
    course_id: UUID
    status: str  # or Literal["active", "completed", "cancelled"]
    created_at: datetime
    updated_at: datetime


class ResourceSchema(BaseModel):
    id: UUID
    course_id: UUID
    title: str
    file_url: str
    uploaded_by: UUID
    created_at: datetime
    updated_at: datetime


class RecordingSchema(BaseModel):
    id: UUID
    course_id: UUID
    title: str
    video_url: str
    uploaded_by: UUID
    created_at: datetime
    updated_at: datetime


class NotificationSchema(BaseModel):
    id: UUID
    title: str
    message: str
    sent_to: UUID
    sent_by: UUID
    is_read: bool
    created_at: datetime
    updated_at: datetime



class Role(BaseModel):
    id: str
    permissions: List[str]


class User(BaseModel):
    id: UUID
    email: EmailStr
    role: Role
    has2FA: bool
    isVerified: bool
    isActive: bool
    createdAt: datetime
    updatedAt: datetime
    lastLogin: datetime
    isAdmin: bool
