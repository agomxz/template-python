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
    created_at = Column(Date, index=True)
    position_id = Column(Integer, index=True)

class Position(Base):
    __tablename__ = 'position'
    position_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)


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

class Match(Base):
    __tablename__ = 'match'
    match_id = Column(Integer, primary_key=True, index=True)
    team_local = Column(Integer, index=True)
    team_visitor = Column(Integer, index=True)
    date = Column(Date, index=True)
    score_local = Column(Integer, index=True)
    score_visitor = Column(Integer, index=True)
    winner = Column(Integer, index=True)
    loser = Column(Integer, index=True)
    draw = Column(Boolean(), default=False)
    played = Column(Boolean(), default=False)
    tournament_id = Column(Integer, index=True)
    stadium_id = Column(Integer, index=True)
    referee_id = Column(Integer, index=True)
    is_active = Column(Boolean(), default=True)