import pandas as pd


class DataLoader:
    """
    Responsible for loading and validating CSV datasets.
    This is the first step in the agent pipeline.
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_csv(self) -> pd.DataFrame:
        """
        Loads a CSV file and returns a pandas DataFrame.

        Raises:
            ValueError: If the file cannot be loaded or is invalid.
        """
        try:
            df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            raise ValueError(f"File not found: {self.file_path}")
        except pd.errors.EmptyDataError:
            raise ValueError("The uploaded CSV file is empty.")
        except pd.errors.ParserError:
            raise ValueError("The uploaded CSV file could not be parsed.")
        except Exception as e:
            raise ValueError(f"Unexpected error while loading CSV: {str(e)}")

        if df.empty:
            raise ValueError("The CSV file contains no rows.")

        if len(df.columns) == 0:
            raise ValueError("The CSV file contains no columns.")

        return df
