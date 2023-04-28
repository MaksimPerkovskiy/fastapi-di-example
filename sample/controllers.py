from fastapi import APIRouter, Depends
from starlette.requests import Request
from sqlalchemy.ext.asyncio import AsyncSession

from .services import UserService
from .dao import UserDAO, PermissionsDAO
from .providers import provide_session_stub


router = APIRouter(prefix='/api', tags=['Users'])


@router.get('/user')
async def users_list(
        session: AsyncSession = Depends(provide_session_stub)
):
    user_service = UserService(
        user_dao=UserDAO(session=session),
        permissions_dao=PermissionsDAO(session=session),
        session=session
    )
    await user_service.get_users_list()


@router.get('/user/{user_id}')
async def user(
        request: Request,
        user_id: int,
        session: AsyncSession = Depends(provide_session_stub)
):
    request.state.session = session
    user_service = UserService(
        user_dao=UserDAO(session=session),
        permissions_dao=PermissionsDAO(session=session),
        session=session
    )
    raise ValueError
    await user_service.get_user(user_id=user_id)
