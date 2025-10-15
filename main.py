from datetime import datetime, timedelta
from planner.tasks import Task
from planner.htn import HTNPlanner
from planner.llm_interface import generate_tasks_from_goal

import re

def parse_llm_tasks(llm_text):
    """
    Parse hierarchical LLM output into structured tasks.
    Returns a list of dicts: [{'task': str, 'duration': float, 'dependencies': list}]
    """
    tasks = []
    lines = llm_text.split("\n")
    parent_stack = []

    for line in lines:
        # Ignore empty lines
        if not line.strip():
            continue

        # Match task lines (with bullet points or numbering)
        match = re.match(r"[-*]\s*(Subtask\s*\d+\.?\d*|Task Name):?\s*(.*)", line)
        if match:
            task_name = match.group(2).strip()

            # Try to extract duration from line
            duration_match = re.search(r"(\d+)\s*(hours|days|business days)", line, re.IGNORECASE)
            if duration_match and duration_match.group(1).isdigit():
                duration = float(duration_match.group(1))
                if "hour" in duration_match.group(2).lower():
                    duration = duration / 8  # convert hours to days
            else:
                duration = 1  # default if missing

            # Determine parent task (if any)
            level = line.count("    ")  # indentation for hierarchy
            if level == 0:
                parent_stack = [task_name]
                dependencies = []
            else:
                dependencies = [parent_stack[-1]] if parent_stack else []
                if len(parent_stack) <= level:
                    parent_stack.append(task_name)
                else:
                    parent_stack[level] = task_name

            tasks.append({
                "task": task_name,
                "duration": duration,
                "dependencies": dependencies
            })

    return tasks


def main():
    # Step 1: User enters a goal
    goal = input("Enter your goal: ")
    print("\nGenerating tasks using LLM... Please wait.")

    # Step 2: Generate tasks from LLM
    tasks_text = generate_tasks_from_goal(goal)
    print("\nLLM Suggested Tasks:\n", tasks_text)

    # Step 3: Parse tasks
    task_list = parse_llm_tasks(tasks_text)

    # Step 4: Create compound task for planner
    compound_task = Task(goal, subtasks=task_list)

    # Step 5: Generate plan using HTN
    planner = HTNPlanner()
    plan = planner.create_plan(compound_task)

    # Step 6: Display plan
    print("\nGenerated Smart Plan:")
    for step in plan:
        start = step['start'].strftime('%d-%m %H:%M')
        end = step['end'].strftime('%d-%m %H:%M')
        print(f"{step['task']}: {start} -> {end}")


if __name__ == "__main__":
    main()

