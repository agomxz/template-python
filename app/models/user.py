from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, Date
from sqlalchemy.orm import relationship

#from db.base_class import Base
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    role_id = Column(Integer, index=True)

class Role(Base):
    __tablename__ = 'role'

    role_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)


class Team(Base):
    __tablename__ = 'team'
    team_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    foundation_date = Column(Date, index=True)
    logo = Column(String, index=True)


class UserTeam(Base):
    __tablename__ = 'user_team'
    user_team_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    team_id = Column(Integer, index=True)


