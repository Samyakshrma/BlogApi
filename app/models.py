from pydantic import BaseModel, Field
from typing import Optional

class BlogPost(BaseModel):
    title: str = Field(..., max_length=100)
    content: str
    author: str
    tags: Optional[list[str]] = []
    published: Optional[bool] = False
