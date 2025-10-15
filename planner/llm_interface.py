import google.generativeai as genai

# Configure your valid Gemini API key
genai.configure(api_key="AIzaSyCYP04KfIAMWvIRmcsUscNyQqB7zZ-hbDc")

def generate_tasks_from_goal(goal):
    """
    Generates hierarchical tasks with estimated times & deadlines using Gemini.
    """
    # Use the available model
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    You are a smart Hybrid HTN planner.
    User goal: "{goal}"

    Break this goal into a hierarchical list of tasks with:
    - Task name
    - Subtasks (if any)
    - Estimated time (hours/days)
    - Dependencies
    - Suggested deadlines

    Format output clearly for reading.
    """

    response = model.generate_content(prompt)
    return response.text.strip()

