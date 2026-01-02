from data_loader import DataLoader
from data_profiler import DataProfiler
from insight_rules import InsightRules
from visualization_engine import VisualizationEngine
from chart_selector import ChartSelector

# Load data
loader = DataLoader("test.csv")
df = loader.load_csv()

# Profile data
profiler = DataProfiler(df)
profile = profiler.profile()

# Generate insights
rules = InsightRules(df, profile)
insights = rules.generate_insights()

# Create visualization engine and selector
viz = VisualizationEngine(df)
selector = ChartSelector(viz)

# Render charts based on insights
for insight in insights:
    # For this dataset, sales is our numeric column
    selector.render_chart(insight, numeric_col="sales")
