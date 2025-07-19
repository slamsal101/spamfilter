import pandas as pd
import plotly.express as px

# Define the tasks and their start/end dates
tasks = [
    {"Task": "1. Planning and requirements gathering", "Start": "2025-05-15", "Finish": "2025-05-29"},
    {"Task": "2. System design", "Start": "2025-05-30", "Finish": "2025-06-13"},
    {"Task": "3. System development", "Start": "2025-06-14", "Finish": "2025-07-19"},
    {"Task": "4. Implementation", "Start": "2025-07-20", "Finish": "2025-07-31"},
    {"Task": "5. Testing and debugging", "Start": "2025-08-01", "Finish": "2025-08-10"},
    {"Task": "6. Documentation", "Start": "2025-08-11", "Finish": "2025-08-15"},
]

# Create DataFrame
df = pd.DataFrame(tasks)

# Create Gantt chart
fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Project Timeline (May 15 - August 15, 2025)",
                  labels={"Task": "Project Tasks"}, color="Task")

# Ensure tasks are in serial order from 1 to 6 (top to bottom)
fig.update_yaxes(
    categoryorder="array",
    categoryarray=[
        "6. Documentation",
        "5. Testing and debugging",
        "4. Implementation",
        "3. System development",
        "2. System design",
        "1. Planning and requirements gathering"
    ]
)


fig.show()
