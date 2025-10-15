# Smart Task Planner

Smart Task Planner breaks down user goals into actionable tasks with timelines using AI reasoning. It combines task generation, hierarchical task planning, and intuitive frontends to help users plan and track their goals effectively.

It supports CLI, Streamlit frontend, REST API, and persistent storage via SQLite.

🚀 Features

Generate tasks from a high-level goal using AI (LLM-based)

Parse and manage hierarchical tasks

Plan tasks using Hierarchical Task Network (HTN) planner

Store, retrieve, and update tasks through a REST API

Intuitive frontend UI with Streamlit

Persistent storage with SQLite

🛠️ Installation
# Clone the repository
git clone https://github.com/YOUR_USERNAME/smart-task-planner.git
cd smart-task-planner

# Install dependencies
pip install -r requirements.txt

📂 Project Structure
smart-task-planner/
│
├─ main.py                # Optional CLI runner
├─ frontend.py            # Streamlit UI
├─ api.py                 # FastAPI backend
├─ requirements.txt       # Python dependencies
├─ tasks.db               # SQLite database (auto-created)
└─ planner/               # Python package for logic
    ├─ __init__.py
    ├─ parser.py          # Parse LLM text
    ├─ tasks.py           # Task class
    ├─ htn.py             # HTN planner
    └─ llm_interface.py   # LLM interaction

🖥️ Usage
1. CLI
python main.py --goal "Plan my study schedule for exams"

2. Streamlit Frontend
streamlit run frontend.py

3. REST API
uvicorn api:app --reload


POST /tasks/ → Add a new goal

GET /tasks/ → Retrieve all tasks

GET /tasks/{task_id} → Retrieve a specific task

📌 Example: Planning a Product Launch

Query:

Plan a product launch in 2 weeks

CLI Usage
python main.py --goal "Plan a product launch in 2 weeks"


Sample Output:

Task 1: Define target audience (2 days)
Task 2: Design marketing materials (3 days)
Task 3: Prepare product demo (2 days)
Task 4: Set up launch event (3 days)
Task 5: Execute marketing campaign (2 days)
Task 6: Gather feedback post-launch (1 day)

Streamlit Frontend

Enter the goal: "Plan a product launch in 2 weeks"

Click Generate Tasks

Tasks appear in a hierarchical timeline view

Mark subtasks as completed as you progress

REST API Example
POST /tasks/
{
  "goal": "Plan a product launch in 2 weeks"
}


Response:

{
  "task_id": 101,
  "goal": "Plan a product launch in 2 weeks",
  "tasks": [
    {"name": "Define target audience", "duration": "2 days"},
    {"name": "Design marketing materials", "duration": "3 days"},
    {"name": "Prepare product demo", "duration": "2 days"},
    {"name": "Set up launch event", "duration": "3 days"},
    {"name": "Execute marketing campaign", "duration": "2 days"},
    {"name": "Gather feedback post-launch", "duration": "1 day"}
  ]
}

<img width="882" height="821" alt="image" src="https://github.com/user-attachments/assets/de16e23c-ccb9-4407-94ba-49aa0fc10281" />




🎥 Demo Video
https://drive.google.com/file/d/1l5xZc29_rUZwDvnaUl1PsEi2IPIr-v3H/view?usp=drive_link

Watch the Demo

💡 How it Works

Goal Input: User provides a high-level goal

Task Generation: LLM generates a list of tasks

Task Parsing: Tasks are parsed into hierarchical subtasks using planner/parser.py

Task Planning: HTN planner (planner/htn.py) schedules tasks based on dependencies

Storage & Retrieval: Tasks are stored in SQLite (tasks.db) and can be retrieved via REST API or UI

🛠️ Technologies Used

Python 3.11+

FastAPI (REST API)

Streamlit (Frontend)

SQLite (Database)

OpenAI / LLM (Task generation)

HTN Planner (Task scheduling)

🤝 Contribution

Contributions are welcome!

Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License

This project is licensed under the MIT License – see the LICENSE
 file for details.
