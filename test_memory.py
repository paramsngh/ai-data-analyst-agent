from memory import AgentMemory

memory = AgentMemory()

memory.store_dataset("test.csv")
memory.store_profile({"columns": {"sales": {"type": "numeric"}}})

insights = [
    {"type": "numeric_summary", "column": "sales"},
    {"type": "time_series_detected", "column": "date"}
]

memory.store_insights(insights)

print(memory.dataset_path)
print(memory.profile)
print(memory.insights)

memory.mark_rendered("numeric_summary")

print(memory.is_rendered("numeric_summary"))  # True
print(memory.is_rendered("time_series_detected"))  # False
