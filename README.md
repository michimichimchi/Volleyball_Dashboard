# how to run:

1. clone repo
2. create .env file and set these variables:
    - MYSQL_ROOT_PASSWORD
    - MYSQL_DATABASE
    - SECRET_KEY
3. run docker compose up -d --build

- Frontend:  http://localhost:5173
- Backend:   http://localhost:8000
- API-Docs:  http://localhost:8000/docs

Database Model:
```mermaid
erDiagram
    User ||--o{ Match : updates
    Team ||--o{ Match : team_b
    Team ||--o{ Match : team_a

    Team {
        int id PK
        string name
    }
    User {
        int id PK
        string username
        string password_hash
        string role
    }
    Match {
        int id PK
        int team_a_id FK
        int team_b_id FK
        int score_team_a
        int score_team_b
        string phase
        int updated_by_id FK
    }
```