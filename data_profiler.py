import pandas as pd
from typing import Dict, Any


class DataProfiler:
    """
    Analyzes a DataFrame and extracts structural and statistical information.
    """

    def __init__(self, df: pd.DataFrame):
        self.df = df

    def profile(self) -> Dict[str, Any]:
        profile = {
            "row_count": len(self.df),
            "column_count": len(self.df.columns),
            "columns": {},
            "time_columns": []
        }

        for column in self.df.columns:
            series = self.df[column]
            col_info = {}

            col_info["dtype"] = str(series.dtype)
            col_info["missing_values"] = int(series.isna().sum())

            if pd.api.types.is_numeric_dtype(series):
                col_info["type"] = "numeric"
                col_info["mean"] = float(series.mean())
                col_info["min"] = float(series.min())
                col_info["max"] = float(series.max())
                col_info["std"] = float(series.std())

            elif pd.api.types.is_datetime64_any_dtype(series):
                col_info["type"] = "datetime"
                profile["time_columns"].append(column)

            else:
                col_info["type"] = "categorical"
                col_info["unique_values"] = int(series.nunique())
                col_info["top_values"] = series.value_counts().head(3).to_dict()

                if self._looks_like_datetime(series):
                    profile["time_columns"].append(column)

            profile["columns"][column] = col_info

        return profile

    def _looks_like_datetime(self, series: pd.Series) -> bool:
        """
        Heuristic check to see if a column might represent dates.
        """
        try:
            parsed = pd.to_datetime(series.dropna(), errors="coerce")
            success_rate = parsed.notna().mean()
            return success_rate > 0.8
        except Exception:
            return False
