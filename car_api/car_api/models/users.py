from sqlalchemy.orm import Mapped, mapped_column

from car_api.models import Base


class User(Base):
    __tablename__ = 'users'


    