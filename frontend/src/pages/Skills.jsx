import { useEffect, useState } from "react";
import apiClient from "../api/client";

function Skills() {
  const [skills, setSkills] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchSkills = async () => {
      try {
        const response = await apiClient.get("/skills/");
        setSkills(response.data);
      } catch (err) {
        setError("Failed to fetch skills");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchSkills();
  }, []);

  if (loading) return <p>Loading skills...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h2>Skills</h2>
      <ul>
        {skills.map((skill) => (
          <li key={skill.id}>
            {skill.name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Skills;
