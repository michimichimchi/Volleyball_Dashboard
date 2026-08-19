import os
from models import User, Team, Match
from db_engine import SessionLocal

def seed_data():
    session = SessionLocal()
    try:
        if session.query(User).first():
            return
        
        admin_pwd = os.getenv("ADMIN_PASSWORD", "StandardFallback123!")
        feld1_pwd = os.getenv("FELD1_PASSWORD", "StandardFallback123!")
        feld2_pwd = os.getenv("FELD2_PASSWORD", "StandardFallback123!")
        
        admin = User(username="admin", password=admin_pwd, role="Admin")
        feld1 = User(username="Feld1", password=feld1_pwd, role="Schiedsrichter")
        feld2 = User(username="Feld2", password=feld2_pwd, role="Schiedsrichter")

        session.add_all([admin, feld1, feld2])
        session.commit()
    finally:
        session.close()