from pydantic import BaseModel

class RateLimitRequest(BaseModel):
    key : str
    limit : int
    window : int