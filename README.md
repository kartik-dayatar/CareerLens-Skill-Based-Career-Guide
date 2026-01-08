# **CareerLens – Skill Based Career Guide (Backend)**

**This repository contains the backend part of the CareerLens project.**

**The idea of this project is to build a skill-based career guidance system where career recommendations are not only based on degrees or marks, but mainly on actual skills, interests and aptitude, with focus on the Indian job market.**

**This project is currently under development and also acts as a learning project for FastAPI, backend architecture, and database integration.**

***

### Why this project?

Most students (including me) face problems like:

+ confusion while choosing a career path

+ no clarity about which skills are actually required for a role

+ choosing careers only based on marks or trends

+ no idea about realistic salary ranges or learning paths

This project tries to solve that by:

+ taking skill input from users

+ evaluating skills (later using assessments)

+ recommending suitable career roles

+ showing skill gaps and learning roadmap

***

### Current Status

+ Backend setup using FastAPI

+ Project structure created

+ User model and database logic in progress

+ SQLite planned for local development

+ AI / ML features planned for later phases

This is not a finished product yet.
***
### Tech Stack (Planned / Used)

#### Backend

+ Python

+ FastAPI

+ SQLAlchemy

+ SQLite (for local development)

#### Frontend (Later)

+ React

### AI / ML (Later Phase)

+ Recommendation logic

+ LLM based explanations

+ Resume generation
---

### How to Run Locally
#### 1. Clone the repository
   
>git clone https://github.com/kartik-dayatar/CareerLens-Skill-Based-Career-Guide.git
>
>cd CareerLens-Skill-Based-Career-Guide/backend

#### 2. Create virtual environment
   
>python -m venv venv
>venv\Scripts\activate

#### 3. Create virtual environment

>python -m venv venv
>
>venv\Scripts\activate

#### 4. Install dependencies

>pip install -r requirements.txt

#### 5. Run the FastAPI server

>uvicorn app.main:app --reload

### Database

+ SQLite is used for local development

+ SQLAlchemy ORM is used

+ Database tables are created using models

Currently working on:

+ proper engine setup

+ fixing import path issues

+ user table creation
---
### Features Planned

+ User registration & login

+ User profile (education, skills, interests)

+ Skill selection

+ Basic skill assessment

+ Career role recommendation

+ Salary range estimation (LPA)

+ Skill gap identification

+ Basic learning roadmap

+ Simple resume generation
---
### Known Issues / Learning Notes

This project is also part of my learning, so:

+ import errors were faced and fixed

+ FastAPI project structure understanding is in progress

+ database engine reference issues are being worked on

These are expected at this stage.

### Documentation

A detailed Software Requirement Specification (SRS) has been written for this project, which explains:

+ system scope

+ features

+ MVP

+ future enhancements
---
### Future Work

+ AI based skill assessment

+ LLM powered career explanation chatbot

+ Better recommendation logic

+ Internship and course suggestions

+ Frontend integration

+ Deployment
---
### Author

#### Kartik Dayatar
B.Tech Student
Learning Backend Development, AI and Data Science

## Note:

**This project is still under development.**
**Code quality and structure will improve as the project progresses.**
