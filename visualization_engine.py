import pandas as pd
import matplotlib.pyplot as plt


class VisualizationEngine:
    """
    Generates matplotlib figures instead of displaying them.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_numeric_distribution(self, column: str):
        fig, ax = plt.subplots()
        self.df[column].hist(bins=10, ax=ax)
        ax.set_title(f"Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        return fig

    def plot_category_breakdown(self, category_col: str, numeric_col: str):
        grouped = self.df.groupby(category_col)[numeric_col].mean()
        fig, ax = plt.subplots()
        grouped.plot(kind="bar", ax=ax)
        ax.set_title(f"Average {numeric_col} by {category_col}")
        ax.set_xlabel(category_col)
        ax.set_ylabel(f"Average {numeric_col}")
        return fig

    def plot_time_series(self, time_col: str, numeric_col: str):
        df_sorted = self.df.sort_values(time_col)
        fig, ax = plt.subplots()
        ax.plot(df_sorted[time_col], df_sorted[numeric_col])
        ax.set_title(f"{numeric_col} over time")
        ax.set_xlabel(time_col)
        ax.set_ylabel(numeric_col)
        plt.xticks(rotation=45)
        return fig
import pandas as pd
import matplotlib.pyplot as plt


class VisualizationEngine:
    """
    Generates matplotlib figures for different chart types.
    Figures are returned so the UI can render them.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_numeric_distribution(self, column: str):
        fig, ax = plt.subplots()
        self.df[column].hist(bins=10, ax=ax)
        ax.set_title(f"Distribution of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")
        return fig

    def plot_category_breakdown(self, category_col: str, numeric_col: str):
        grouped = self.df.groupby(category_col)[numeric_col].mean()
        fig, ax = plt.subplots()
        grouped.plot(kind="bar", ax=ax)
        ax.set_title(f"Average {numeric_col} by {category_col}")
        ax.set_xlabel(category_col)
        ax.set_ylabel(f"Average {numeric_col}")
        return fig

    def plot_time_series(self, time_col: str, numeric_col: str):
        df_sorted = self.df.sort_values(time_col)
        fig, ax = plt.subplots()
        ax.plot(df_sorted[time_col], df_sorted[numeric_col])
        ax.set_title(f"{numeric_col} over time")
        ax.set_xlabel(time_col)
        ax.set_ylabel(numeric_col)
        plt.xticks(rotation=45)
        return fig
