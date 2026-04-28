from pydantic import BaseModel

class UserBase (BaseModel):
    email: str

class UserCreate (UserBase):
    password: str 

class UserOut (UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class HabitBase (BaseModel):
    title: str
    description: str
    is_completed:bool = False

class HabitCreate (HabitBase):
    pass
class HabitOut (HabitBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True