from data_loader import DataLoader
from data_profiler import DataProfiler
from insight_rules import InsightRules

loader = DataLoader("test.csv")
df = loader.load_csv()

profiler = DataProfiler(df)
profile = profiler.profile()

rules = InsightRules(df, profile)
insights = rules.generate_insights()

for insight in insights:
    print(insight)
