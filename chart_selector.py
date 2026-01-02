class ChartSelector:
    """
    Selects the appropriate chart based on an insight.
    Returns matplotlib figures.
    """

    def __init__(self, viz_engine):
        self.viz = viz_engine

    def render_chart(self, insight, numeric_col=None):
        insight_type = insight["type"]
        column = insight["column"]

        if insight_type == "numeric_summary":
            return self.viz.plot_numeric_distribution(column)

        elif insight_type == "category_dominance":
            return self.viz.plot_category_breakdown(column, numeric_col)

        elif insight_type == "time_series_detected":
            return self.viz.plot_time_series(column, numeric_col)

        return None
