from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):
    id : int
    name : str
    age : int
    phone : str
    salary : int
    role : str
    email : str
    created_at : datetime
    
    model_config = ConfigDict(from_attributes=True)