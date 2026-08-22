import os
from models import User, Team, Match
from db_engine import SessionLocal, engine
import pandas as pd
import random

def seed_data():
    session = SessionLocal()
    try:
        if not session.query(User).first():
            # seed users
            admin_pwd = os.getenv("ADMIN_PASSWORD", "StandardFallback123!")
            feld1_pwd = os.getenv("FELD1_PASSWORD", "StandardFallback123!")
            feld2_pwd = os.getenv("FELD2_PASSWORD", "StandardFallback123!")
            
            df_users = pd.DataFrame({"username": ["admin", "feld1", "feld2"],
                                     "password": [admin_pwd, feld1_pwd, feld2_pwd],
                                     "role": ["Admin", "Schiedsrichter", "Schiedsrichter"]
                                     })
            
            df_users.to_sql("users", con=engine, if_exists="append", index=False)
        
        if not session.query(Team).first():
        # seed teams
            df_teams = pd.DataFrame({"name": [
                "BWÖ",
                "BWRCHÖxEschenBW",
                "Container",
                "BWS since 2014",
                "BW Kidsclub",
                "BW Degernau I",
                "BW Degernau II",
                "BW Meister Proper",
                "BWS - DAS Original",
                "Bauwagen Schwerzen II",
                "Babys Conti",
                "EschenBW est. 2024",
                "Bauwagen Horheim Junior",
                "BW Degernau - 1st Generation",
                "BW Wutachblick"
            ]})
            
            df_teams.to_sql("teams", con=engine, if_exists="append", index=False)
            
            if not session.query(Match).first() and session.query(Team).first():
            # seed group phase matches in random constelation
                all_teams = session.query(Team).all()
                random.shuffle(all_teams)
            
                
    finally:
        session.close()

