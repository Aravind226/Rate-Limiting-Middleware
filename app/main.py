from fastapi import FastAPI
from app.schema import RateLimitRequest
from app.limiter import check_rate_limit
from app.middleware import RateLimitMiddleware

app = FastAPI()
app.add_middleware(RateLimitMiddleware)

@app.get("/")
def home():
    return {"message" : "You made it past the rate limiter"}