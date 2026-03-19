from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from app.limiter import check_rate_limit
from app.api_keys import API_KEYS

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key = request.headers.get("x-api-key")

        if not api_key or api_key not in API_KEYS:
            raise HTTPException(status_code=401, detail="Invalid API key")
        
        config = API_KEYS[api_key]

        route = request.url.path
        key = f"rate_limit:{api_key}:{route}"

        allowed, remaining = check_rate_limit(
            key,
            config["limit"],
            config["window"]

        )

        if not allowed:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        
        response = await call_next(request)

        response.headers["X-RateLimit-Limit"] = str(config["limit"])
        response.headers["X-RateLimit-Remaining"] = str(remaining)

        return response