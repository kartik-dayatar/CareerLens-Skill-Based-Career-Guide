# Define role requirements (static for v1)

ROLES = {
    "Data Analyst": {
        "required_skills": {
            "Python": 7,
            "SQL": 7,
            "Statistics": 6,
            "Communication": 5
        }
    },
    "ML Engineer": {
        "required_skills": {
            "Python": 8,
            "Machine Learning": 7,
            "Linear Algebra": 6,
            "Statistics": 6
        }
    },
    "Backend Developer": {
        "required_skills": {
            "Python": 7,
            "Databases": 6,
            "APIs": 6
        }
    }
}
ROLE_SALARY = {
    "Data Analyst": "5–9 LPA",
    "ML Engineer": "7–14 LPA",
    "Backend Developer": "6–12 LPA"
}


def recommend_roles(user_skills: dict):
    """
    user_skills = {
        "Python": 8,
        "SQL": 6,
        "Statistics": 5
    }
    """

    recommendations = []

    for role, role_data in ROLES.items():
        required_skills = role_data["required_skills"]

        total_required = len(required_skills)
        matched = 0
        skill_gaps = []

        for skill, required_level in required_skills.items():
            user_level = user_skills.get(skill)

            if user_level is None:
                skill_gaps.append(skill)
            elif user_level >= required_level:
                matched += 1
            else:
                skill_gaps.append(skill)

        match_score = round((matched / total_required) * 100, 2)

        recommendations.append({
            "role": role,
            "match_score": match_score,
            "skill_gap_message": f"Improve {', '.join(skill_gaps)} to qualify for this role",
            "salary_range": ROLE_SALARY.get(role, "N/A")
        })

    # Sort by match score (highest first)
    recommendations.sort(key=lambda x: x["match_score"], reverse=True)

    return recommendations

