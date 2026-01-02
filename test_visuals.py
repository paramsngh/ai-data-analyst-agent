from data_loader import DataLoader
from visualization_engine import VisualizationEngine

loader = DataLoader("test.csv")
df = loader.load_csv()

viz = VisualizationEngine(df)

# Test numeric distribution
viz.plot_numeric_distribution("sales")

# Test category breakdown
viz.plot_category_breakdown("region", "sales")

# Test time series
viz.plot_time_series("date", "sales")
