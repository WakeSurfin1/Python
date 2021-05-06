## Pydantic tutorial 
## https://betterprogramming.pub/the-beginners-guide-to-pydantic-ba33b26cde89

from pydantic import BaseModel, ValidationError
from typing import Optional
from typing import List
from datetime import datetime

class User(BaseModel):
    id: int
    username : str
    password : str
    confirm_password : str
    alias = 'anonymous'
    timestamp: Optional[datetime] = None
    friends: List[int] = []

data = {'id': '123', 'username': 'wai foong', 'password': 'Password123', 'confirm_password': 'Password123', 'timestamp': '2020-08-03 10:30', 'friends': [1, '2', b'3']}

try:
    user = User(**data)
    print("test values are correct")
except ValidationError as e:
    print(e.json())

exit()