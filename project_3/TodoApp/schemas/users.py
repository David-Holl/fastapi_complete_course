from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str = Field(min_length=8)
    phone_number: str


class UserRead(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    role: str
    is_active: bool
    phone_number: str


class ChangePasswordRequest(BaseModel):
    old_password: str = Field(min_length=8)
    new_password: str = Field(min_length=8)


class ChangePhoneNumberRequest(BaseModel):
    password: str = Field(min_length=8)
    new_phone_number: str
