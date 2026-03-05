# CareerLens – Project Context (Claude.md)

> **⚠️ AGENT INSTRUCTIONS: Read this file FIRST before doing anything. Update this file after EVERY change/commit you make.**

---

## 1. Project Overview

**CareerLens** is a skill-based career guidance system for the **Indian job market**. Instead of recommending careers based on degrees/marks, it evaluates a user's **actual skills and self-ratings** to recommend suitable career roles, identify skill gaps, and show salary estimates.

- **Author:** Kartik Dayatar (B.Tech Student)
- **Status:** 🟡 Early Development (MVP in progress)
- **Repo:** `CareerLens` (renamed from `CareerLens-Skill-Based-Career-Guide`)

---

## 2. Tech Stack

| Layer | Technology | Version |
|---|---|---|
| Backend Framework | FastAPI | latest |
| ORM | SQLAlchemy | latest |
| Database | PostgreSQL | latest |
| Env Config | python-dotenv | latest |
| DB Driver | psycopg2-binary | latest |
| Validation | Pydantic | latest |
| ASGI Server | Uvicorn | latest |
| Frontend Framework | React | 19.2.0 |
| Build Tool | Vite | 7.2.4 |
| HTTP Client | Axios | 1.13.4 |
| Linting | ESLint | 9.39.1 |

---

## 3. Project Structure

```
CareerLens/
├── .gitignore                     ← Ignores .env, __pycache__, node_modules, etc.
├── Claude.md                      ← THIS FILE (project context for agents)
├── README.md
├── ERRORS_FOUND_AND_FIXED.md      ← (empty)
│
├── backend/
│   ├── .env                       ← DATABASE_URL (not committed to git)
│   ├── requirements.txt           ← fastapi, uvicorn, sqlalchemy, pydantic, psycopg2-binary, python-dotenv
│   └── app/
│       ├── __init__.py
│       ├── main.py                ← FastAPI app entry point, CORS config, router registration
│       ├── database.py            ← PostgreSQL engine via DATABASE_URL env var, SessionLocal, Base, get_db()
│       ├── models/
│       │   ├── __init__.py        ← Exports User, Skill, UserSkill
│       │   ├── user.py            ← User model (id, name, email, education, experience)
│       │   ├── skill.py           ← Skill model (id, name, skill_type)
│       │   └── userskill.py       ← UserSkill model (id, user_id FK, skill_id FK, self_rating)
│       ├── schemas/
│       │   ├── __init__.py        ← Exports all schemas
│       │   ├── user.py            ← UserCreate, UserResponse
│       │   ├── skill.py           ← SkillCreate, SkillBulkCreate, SkillResponse
│       │   └── userskill.py       ← UserSkillCreate, UserSkillResponse
│       ├── api/
│       │   ├── __init__.py
│       │   ├── user.py            ← /users endpoints (POST /, GET /{id}, GET /)
│       │   ├── skill.py           ← /skills endpoints (GET /, POST /, POST /bulk)
│       │   ├── userskill.py       ← /user-skills endpoints (POST /, GET /user/{id})
│       │   └── recommendation.py  ← /recommendations/user/{id} endpoint
│       └── core/
│           ├── __init__.py
│           └── role_recommender.py ← Recommendation engine (hardcoded roles + matching logic)
│
├── frontend/
│   ├── package.json
│   ├── vite.config.js
│   ├── index.html
│   └── src/
│       ├── main.jsx               ← React root render
│       ├── App.jsx                ← Root component (renders <Skills />)
│       ├── index.css              ← Global CSS (basic reset + defaults)
│       ├── api/
│       │   └── client.js          ← Axios instance → http://localhost:8000
│       └── pages/
│           └── Skills.jsx         ← Fetches & displays skills list from backend
```

---

## 4. Database (PostgreSQL)

**Connection:** Via `DATABASE_URL` environment variable in `backend/.env`
```
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/careerlens
```

Three tables with a many-to-many relationship via `user_skills`:

```
users                    skills                   user_skills
+-----------+            +-----------+             +-----------+
| id (PK)   |            | id (PK)   |             | id (PK)   |
| name      |      ┌─────| name (UQ) |──────┐      | user_id   |──→ users.id
| email (UQ)|      │     | skill_type|      │      | skill_id  |──→ skills.id
| education |      │     +-----------+      │      | self_rating| (1-10)
| experience|      │                        │      +-----------+
+-----------+      └────────────────────────-┘
```

- `skill_type` = "technical" or "soft"
- `self_rating` = 1 to 10 (user's self-assessment)

---

## 5. API Endpoints (9 total)

| Method | URL | What It Does |
|---|---|---|
| `GET` | `/` | Health check → `{"message": "CareerLens backend running"}` |
| `POST` | `/users/` | Create user (name, email, education?, experience?) |
| `GET` | `/users/{user_id}` | Get user by ID |
| `GET` | `/users/` | List all users |
| `GET` | `/skills/` | List all skills |
| `POST` | `/skills/` | Create single skill (name, skill_type) |
| `POST` | `/skills/bulk` | Bulk create skills |
| `POST` | `/user-skills/` | Assign skill to user with self_rating |
| `GET` | `/user-skills/user/{user_id}` | Get all skills of a user |
| `GET` | `/recommendations/user/{user_id}` | Get career recommendations |

**CORS:** Allowed origins → `localhost:5174`, `127.0.0.1:5174`

---

## 6. Recommendation Engine (core/role_recommender.py)

Currently **rule-based** with 3 hardcoded roles:

| Role | Required Skills (min rating) | Salary |
|---|---|---|
| Data Analyst | Python(7), SQL(7), Statistics(6), Communication(5) | 5–9 LPA |
| ML Engineer | Python(8), ML(7), Linear Algebra(6), Statistics(6) | 7–14 LPA |
| Backend Developer | Python(7), Databases(6), APIs(6) | 6–12 LPA |

**Logic:** Calculates match_score = (matched skills / total required) × 100, identifies skill gaps, returns sorted list.

---

## 7. How to Run

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Make sure PostgreSQL is running and "careerlens" database exists
# Edit .env with your PostgreSQL password if needed
uvicorn app.main:app --reload
# Runs on http://localhost:8000
# Swagger docs: http://localhost:8000/docs
```

### Frontend
```bash
cd frontend
npm install
npm run dev
# Runs on http://localhost:5174
```

---

## 8. Progress Tracker

### ✅ Completed
- [x] FastAPI project structure set up
- [x] SQLAlchemy + PostgreSQL database integration (migrated from SQLite)
- [x] Environment variable config for DATABASE_URL (.env + python-dotenv)
- [x] Root .gitignore to protect secrets
- [x] User model + CRUD API (create, get by id, get all)
- [x] Skill model + CRUD API (create, bulk create, get all)
- [x] UserSkill junction model + API (assign skill to user, get user skills)
- [x] Rule-based career recommendation engine (3 roles)
- [x] Recommendation API endpoint
- [x] CORS middleware configured
- [x] React + Vite frontend initialized
- [x] Axios API client setup
- [x] Skills list page (fetches and displays skills)
- [x] Basic CSS reset / global styles

### 🔲 Remaining (TODO)
- [ ] **Auth:** User registration & login (JWT or similar)
- [ ] **Frontend Pages:**
  - [ ] User registration / login page
  - [ ] User profile page (education, skills, interests)
  - [ ] Skill selection UI (pick skills + rate them)
  - [ ] Recommendation results page (show match scores, gaps, salaries)
  - [ ] Learning roadmap page
- [ ] **Frontend:** React Router setup for navigation
- [ ] **Frontend:** Proper component library / design system
- [ ] **Backend:** More career roles in the recommendation engine
- [ ] **Backend:** Skill assessment / quiz system
- [ ] **AI/ML:** Replace hardcoded rules with ML-based recommendation
- [ ] **AI/ML:** LLM-powered career explanation chatbot
- [ ] **Feature:** Resume generation
- [ ] **Feature:** Internship & course suggestions
- [ ] **Deployment:** Production deployment setup

---

## 9. Key Architecture Notes

1. **Backend follows a clean layered pattern:** `api/` (routes) → `schemas/` (validation) → `models/` (ORM) → `database.py` (connection)
2. **Database URL is loaded from `.env`** via `python-dotenv` — never hardcode credentials
3. **Recommendation logic is isolated** in `core/role_recommender.py` — easy to swap out with ML later
4. **Frontend currently has no routing** — just renders `<Skills />` directly in `App.jsx`
5. **CORS is set to port 5174** — if Vite picks a different port, update `main.py`
6. **No auth exists yet** — all endpoints are publicly accessible
7. **Database tables are auto-created** on app startup via `Base.metadata.create_all()`
8. **PostgreSQL must be running** before starting the backend

---

## 10. Changelog

| Date | Changes |
|---|---|
| 2026-03-05 | Claude.md created. Project analyzed. All backend CRUD + recommendation engine working. Frontend has Skills page only. |
| 2026-03-06 | Migrated database from SQLite → PostgreSQL. Added psycopg2-binary + python-dotenv to requirements. Created .env for DATABASE_URL. Created root .gitignore. Renamed GitHub repo to `CareerLens`. |

---

> **🔁 REMINDER TO AGENTS: After making ANY changes to this project, update sections 3 (structure), 8 (progress), and 10 (changelog) in this file.**
