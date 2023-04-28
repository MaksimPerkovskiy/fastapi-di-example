from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST
from functools import wraps
from typing import Callable, ParamSpec, TypeVar


RT = TypeVar('RT')
P = ParamSpec('P')


def finalize_session(func: Callable[P, RT]) -> Callable[P, RT]:
    @wraps(func)
    async def wrap(request: Request, *args: P.args, **kwargs: P.kwargs) -> RT:
        if request.state.session:
            await request.state.session.close()
        
        return await func(request, *args, **kwargs)
    return wrap


@finalize_session
async def http400_error_handler(
        request: Request, 
        exc: ValueError
) -> JSONResponse:
    headers = {"Cache-Control": "no-store", "Pragma": "no-cache"}
    content = {"error": "error"}
    return JSONResponse(
        content=content,
        headers=headers,
        status_code=HTTP_400_BAD_REQUEST
    )
