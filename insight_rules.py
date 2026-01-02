# We use typing to make it clear what kind of data our functions return
from typing import List, Dict, Any

# Pandas is used only to pass the dataframe around (no heavy analysis here)
import pandas as pd


class InsightRules:
    """
    This class applies simple, human-like rules to the dataset
    to detect basic insights.

    Think of this as:
    "What obvious things would a junior data analyst notice?"
    """

    def __init__(self, df: pd.DataFrame, profile: Dict[str, Any]):
        # Store the raw dataframe
        self.df = df

        # Store the profiler output (the dictionary from data_profiler.py)
        self.profile = profile

    def generate_insights(self) -> List[Dict[str, Any]]:
        """
        This is the main function that the agent will call.
        It combines multiple simple insight checks.
        """

        # This list will hold all detected insights
        insights = []

        # Detect numeric columns that are suitable for analysis
        insights.extend(self._detect_numeric_columns())

        # Detect dominant values in categorical columns
        insights.extend(self._detect_categorical_dominance())

        # Detect whether the dataset supports time-based analysis
        insights.extend(self._detect_time_series())

        # Return the final list of insights
        return insights

    def _detect_numeric_columns(self) -> List[Dict[str, Any]]:
        """
        This function checks which columns are numeric.

        Numeric columns are important because:
        - They can be averaged
        - They can be plotted
        - They can show trends
        """

        insights = []

        # Loop through every column found by the profiler
        for column, info in self.profile["columns"].items():

            # If the profiler says the column is numeric
            if info["type"] == "numeric":

                # Add a simple insight explaining this
                insights.append({
                    "type": "numeric_summary",
                    "column": column,
                    "message": f"{column} is a numeric column suitable for analysis."
                })

        return insights

    def _detect_categorical_dominance(self) -> List[Dict[str, Any]]:
        """
        This function checks categorical columns (like region, product, category)
        and finds which value appears most often.

        IMPORTANT:
        We explicitly skip time columns (like dates),
        because dates should not be treated like categories.
        """

        insights = []

        # Convert time columns list to a set for fast lookup
        time_columns = set(self.profile["time_columns"])

        # Loop through all columns
        for column, info in self.profile["columns"].items():

            # We only want:
            # - categorical columns
            # - that are NOT time columns
            # - that have top_values information
            if (
                info["type"] == "categorical"
                and column not in time_columns
                and "top_values" in info
            ):
                top_values = info["top_values"]

                # If the column actually has values
                if top_values:
                    # Find the value that appears the most
                    top_category = max(top_values, key=top_values.get)

                    # Add an insight describing the dominance
                    insights.append({
                        "type": "category_dominance",
                        "column": column,
                        "message": f"{top_category} is the most common value in {column}."
                    })

        return insights

    def _detect_time_series(self) -> List[Dict[str, Any]]:
        """
        This function checks whether the dataset supports time-based analysis.

        If a column looks like time (dates),
        we mark it as suitable for trend analysis.
        """

        insights = []

        # Loop through all detected time columns
        for time_col in self.profile["time_columns"]:

            # Add an insight saying this column can be used for trends
            insights.append({
                "type": "time_series_detected",
                "column": time_col,
                "message": f"{time_col} can be used for time-based trend analysis."
            })

        return insights
