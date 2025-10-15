from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from planner.llm_interface import generate_tasks_from_goal
from planner.parser import parse_llm_tasks

app = FastAPI()

DB_FILE = "tasks.db"

# Initialize database
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal TEXT,
    tasks TEXT
)
""")
conn.commit()
conn.close()

class GoalRequest(BaseModel):
    goal: str

@app.post("/generate_tasks")
def generate_tasks(request: GoalRequest):
    tasks_text = generate_tasks_from_goal(request.goal)
    task_list = parse_llm_tasks(tasks_text)

    # Store in DB
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO tasks (goal, tasks) VALUES (?, ?)", (request.goal, str(task_list)))
    conn.commit()
    conn.close()

    return {"goal": request.goal, "tasks": task_list}

@app.get("/tasks")
def get_all_tasks():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT id, goal, tasks FROM tasks")
    rows = c.fetchall()
    conn.close()
    return [{"id": r[0], "goal": r[1], "tasks": r[2]} for r in rows]

