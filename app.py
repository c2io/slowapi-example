from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

# from slowapi.util import get_remote_address


app = FastAPI()


def limiter_key_func(request: Request) -> str:
    """
    限制 匹配的key方法
    """
    return "127.0.0.1"


limiter = Limiter(key_func=limiter_key_func)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/")
@limiter.limit("100/second")
async def root(request: Request):
    return {"hello": "world"}
