import streamlit as st
from planner.llm_interface import generate_tasks_from_goal
from main import parse_llm_tasks

st.title("🧠 Smart Task Planner")

goal = st.text_input("Enter your goal:")

if st.button("Generate Plan"):
    if not goal.strip():
        st.warning("Please enter a valid goal!")
    else:
        with st.spinner("Generating tasks using LLM..."):
            # Generate tasks from LLM
            tasks_text = generate_tasks_from_goal(goal)

        st.subheader("LLM Suggested Tasks")
        st.text_area("Tasks Text", tasks_text, height=400)

        # Parse tasks
        task_list = parse_llm_tasks(tasks_text)
        st.subheader("Parsed Structured Tasks")
        st.json(task_list)

