from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from car_api.core.database import get_session
from car_api.models.users import User
from car_api.schemas.users import (
    UserSchema,
    UserUpdateSchema,
    UserListPublicSchema,
    UserPublicSchema,
)

router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserPublicSchema)
async def create_user(
    user: UserSchema,
    session: AsyncSession = Depends(get_session),
):
    db_user = User(username=user.username, email=user.email, password=user.password)
    session.add(db_user)
    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='username or email already exists',
        )
    await session.refresh(db_user)
    return db_user


@router.get('/', status_code=status.HTTP_200_OK, response_model=UserListPublicSchema)
async def list_users(session: AsyncSession = Depends(get_session)):
    result = await session.scalars(select(User))
    return {'users': result.all()}


@router.put('/{user_id}', status_code=status.HTTP_201_CREATED, response_model=UserPublicSchema)
async def update_user(
    user_id: int,
    user: UserUpdateSchema,
    session: AsyncSession = Depends(get_session),
):
    db_user = await session.get(User, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    for field, value in user.model_dump(exclude_unset=True).items():
        setattr(db_user, field, value)
    await session.commit()
    await session.refresh(db_user)
    return db_user


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, session: AsyncSession = Depends(get_session)):
    db_user = await session.get(User, user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    await session.delete(db_user)
    await session.commit()
