from pathlib import Path
import pandas as pd

# Project root: jobscope-india/
ROOT = Path(__file__).resolve().parents[2]

DATA_PATH = ROOT / "data" / "processed" / "cleaned_job_market.csv"


def load_job_data():
    """
    Loads the cleaned dataset and returns:
    (DataFrame, None)
    """

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found:\n{DATA_PATH}"
        )

    df = pd.read_csv(DATA_PATH)

    return df, None

print(DATA_PATH)
print(DATA_PATH.exists())
