from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.user import create_user, get_user, get_users
from app.database.dependencies import get_db
from app.schemas.user import UserCreate, UserRead

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=UserRead)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return create_user(db, user)


@router.get("/", response_model=list[UserRead])
def list_users(
    db: Session = Depends(get_db),
):
    return get_users(db)


@router.get("/{user_id}", response_model=UserRead)
def get_single_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = get_user(db, user_id)

    if user is None:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user
