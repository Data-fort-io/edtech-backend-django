from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime


class CourseSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    created_by: int
    is_active: bool
    created_at: datetime
    updated_at: datetime


class EnrollmentSchema(BaseModel):
    id: int
    user_id: int
    course_id: int
    status: str  # optionally: Literal["active", "completed", "cancelled"]
    created_at: datetime
    updated_at: datetime


class ResourceSchema(BaseModel):
    id: int
    course_id: int
    title: str
    file_url: str
    uploaded_by: int
    created_at: datetime
    updated_at: datetime


class RecordingSchema(BaseModel):
    id: int
    course_id: int
    title: str
    video_url: str
    uploaded_by: int
    created_at: datetime
    updated_at: datetime


class NotificationSchema(BaseModel):
    id: int
    title: str
    message: str
    sent_to: int
    sent_by: int
    is_read: bool
    created_at: datetime
    updated_at: datetime


class Role(BaseModel):
    id: str
    permissions: List[str]


class User(BaseModel):
    id: int
    email: EmailStr
    role: Role
    has2FA: bool
    isVerified: bool
    isActive: bool
    createdAt: datetime
    updatedAt: datetime
    lastLogin: datetime
    isAdmin: bool
