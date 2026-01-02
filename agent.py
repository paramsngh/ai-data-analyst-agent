from data_loader import DataLoader
from data_profiler import DataProfiler
from insight_rules import InsightRules
from visualization_engine import VisualizationEngine
from chart_selector import ChartSelector
from memory import AgentMemory


class DataAnalysisAgent:
    """
    Orchestrates the full data analysis pipeline
    while maintaining internal memory.
    """

    def __init__(self, csv_path: str):
        # Store CSV path
        self.csv_path = csv_path

        # Initialize agent memory
        self.memory = AgentMemory()

        # These will be populated during analysis
        self.df = None

    def analyze(self):
        """
        Runs the full analysis pipeline with memory awareness.
        """

        # Step 1: Load data
        loader = DataLoader(self.csv_path)
        self.df = loader.load_csv()

        # Store dataset in memory
        self.memory.store_dataset(self.csv_path)

        # Step 2: Profile data
        profiler = DataProfiler(self.df)
        profile = profiler.profile()

        # Store profile in memory
        self.memory.store_profile(profile)

        # Step 3: Generate insights
        rules = InsightRules(self.df, profile)
        insights = rules.generate_insights()

        # Store insights in memory
        self.memory.store_insights(insights)

        # Step 4: Setup visualization tools
        viz_engine = VisualizationEngine(self.df)
        chart_selector = ChartSelector(viz_engine)

        # Step 5: Render charts, skipping already-rendered insights
        numeric_col = self._get_default_numeric_column(profile)

        for insight in insights:
            insight_type = insight["type"]

            # Skip charts that were already shown
            if self.memory.is_rendered(insight_type):
                continue

            # Render chart
            chart_selector.render_chart(insight, numeric_col=numeric_col)

            # Mark insight as rendered
            self.memory.mark_rendered(insight_type)

    def _get_default_numeric_column(self, profile):
        """
        Selects the first numeric column found in the dataset.
        """

        for column, info in profile["columns"].items():
            if info["type"] == "numeric":
                return column

        raise ValueError("No numeric column found for visualization.")
