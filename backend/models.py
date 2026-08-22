from sqlalchemy import Column, Integer, String, ForeignKey
from db_engine import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    
class Match(Base):
    __tablename__ = "matches"
    
    id = Column(Integer, primary_key=True, index=True)
    team_a = Column(Integer, ForeignKey("teams.id"), nullable=False)
    team_b = Column(Integer, ForeignKey("teams.id"), nullable=False)
    score_team_a = Column(Integer)
    score_team_b = Column(Integer)
    phase = Column(String(100), nullable=False)
    field = Column(String(50))
    updated_by = Column(Integer, ForeignKey("users.id"))
