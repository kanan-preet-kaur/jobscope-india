import pandas as pd


def get_dashboard_metrics(df: pd.DataFrame) -> dict:
    """
    Compute all dashboard KPIs from the dataset.
    """

    metrics = {}

    # -------------------------
    # Dataset Size
    # -------------------------

    metrics["total_jobs"] = len(df)

    # -------------------------
    # Companies
    # -------------------------

    metrics["total_companies"] = (
        df["companyName"]
        .dropna()
        .nunique()
    )

    # -------------------------
    # Locations
    # -------------------------

    metrics["total_locations"] = (
        df["location"]
        .dropna()
        .nunique()
    )

    # -------------------------
    # Skills
    # -------------------------

    skills = (
        df["tagsAndSkills"]
        .dropna()
        .astype(str)
        .str.split(",")
        .explode()
        .str.strip()
    )

    metrics["total_unique_skills"] = skills.nunique()

    return metrics