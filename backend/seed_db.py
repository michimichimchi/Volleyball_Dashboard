import os
from models import User, Team, Match
from db_engine import SessionLocal, engine
import pandas as pd
import random
from auth import get_password_hash

def seed_data():
    session = SessionLocal()
    try:
        if not session.query(User).first():
            # seed users
            admin_pwd = get_password_hash(os.getenv("ADMIN_PASSWORD"))
            feld1_pwd = get_password_hash(os.getenv("FELD1_PASSWORD"))
            feld2_pwd = get_password_hash(os.getenv("FELD2_PASSWORD"))
            
            df_users = pd.DataFrame({"username": ["admin", "feld1", "feld2"],
                                     "password": [admin_pwd, feld1_pwd, feld2_pwd],
                                     "role": ["Admin", "Schiedsrichter", "Schiedsrichter"]
                                     })
            
            df_users.to_sql("users", con=engine, if_exists="append", index=False)
            session.commit()
        
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
            session.commit()
            
        if not session.query(Match).first() and session.query(Team).first():
        # seed group phase matches in random constelation
            all_teams = session.query(Team).all()
            random.shuffle(all_teams)
            
            # seperate teams in two groups
            mid = (len(all_teams) + 1) // 2
            group_a = all_teams[:mid]
            group_b = all_teams[mid:]
        
            df_matches = pd.DataFrame({"team_a": [], "team_b": [], "phase": [], "field": [], "time": []})
            
            # round robin algorithm
            # this algorithm devides the teams in two groups and creates a matchplan for the groupphase where every
            # team plays every other in its group with maximum waiting time for each team between the matches (very proud)
            gametime = pd.Timestamp("2027-03-27 12:00")
            if len(group_a) % 2 != 0:
                group_a.append(None)
            n = len(group_a)
            for _ in range(n -1):
                for i in range(n  // 2):
                    if group_a[i] is not None and group_a[n - 1 - i] is not None:
                        df_matches.loc[len(df_matches)] = [group_a[i].id, group_a[n - 1 - i].id, "Group A", 1, gametime]
                        gametime += pd.Timedelta(minutes=15)
                group_a = [group_a[0]] + [group_a[-1]] + group_a[1:-1]
                
            gametime = pd.Timestamp("2027-03-27 12:00")
            if len(group_b) % 2 != 0:
                group_b.append(None)
            n = len(group_b)
            for _ in range(n -1):
                for i in range(n  // 2):
                    if group_b[i] is not None and group_b[n - 1 - i] is not None:
                        df_matches.loc[len(df_matches)] = [group_b[i].id, group_b[n - 1 - i].id, "Group B", 2, gametime]
                        gametime += pd.Timedelta(minutes=15)
                group_b = [group_b[0]] + [group_b[-1]] + group_b[1:-1]
            
            df_matches.to_sql("matches", con=engine, if_exists="append", index=False)
            session.commit()
                
    finally:
        session.close()

