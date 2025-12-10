from fastapi import HTTPException
from project_3.TodoApp.orm_models.users import Users
from sqlalchemy.orm import Session
from project_3.TodoApp.core.security import bcrypt_context
from starlette import status


class UserService:
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> Users:
        user = db.query(Users).filter(Users.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    @staticmethod
    def authenticate(username: str, password: str, db: Session) -> Users:
        user = db.query(Users).filter(Users.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        if not bcrypt_context.verify(password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return user

    @staticmethod
    def change_password(db: Session, user_id: int, old: str, new: str) -> None:
        user = UserService.get_user_by_id(db, user_id)
        if not bcrypt_context.verify(old, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Old password incorrect",
            )
        user.hashed_password = bcrypt_context.hash(new)
        db.commit()

    @staticmethod
    def change_phone_number(
        db: Session, user_id: int, password: str, new_phone: str
    ) -> None:
        user = UserService.get_user_by_id(db, user_id)
        if not bcrypt_context.verify(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Password incorrect",
            )

        user.phone_number = new_phone
        db.commit()
