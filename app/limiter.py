import time
from app.redis_client import redis_client

with open("app/lua/sliding_window.lua", "r") as f:
    lua_script = f.read()

rate_limiter = redis_client.register_script(lua_script)

def check_rate_limit(key: str, limit: int, window: int):
    now = int(time.time() * 1000)

    result = rate_limiter(
        keys=[key],
        args=[now, window, limit]
    )

    allowed = bool(result[0])
    remaining = int(result[1])

    return allowed,remaining
