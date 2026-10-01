import pandas as pd
import numpy as np

def run_data_pipeline():
    # 1. Fetch raw messy dataset directly from the web
    print("Fetching raw dataset...")
    raw_url = "https://raw.githubusercontent.com/eyowhite/Messy-dataset/main/Uncleaned_DS_jobs.csv"
    df_raw = pd.read_csv(raw_url)

    # 2. Save the unmodified raw dataset locally
    df_raw.to_csv("raw_data.csv", index=False)
    print("Saved original data to 'raw_data.csv'")

    # Make a copy for cleaning operations
    df = df_raw.copy()

    # 3. Drop duplicates and index column
    df = df.drop_duplicates()
    if "index" in df.columns:
        df = df.drop(columns=["index"])

    # 4. Clean missing value placeholders (-1, Unknown -> NaN)
    df = df.replace([-1, "-1", "-1.0", "Unknown", "unknown"], np.nan)

    # 5. Clean Company Name (Removes trailing newline ratings like \n3.8)
    if "Company Name" in df.columns:
        df["Company Name"] = df["Company Name"].apply(
            lambda x: str(x).split("\n")[0].strip() if pd.notna(x) else x
        )

    # 6. Extract state code from Location
    if "Location" in df.columns:
        df["job_state"] = df["Location"].apply(
            lambda x: str(x).split(",")[-1].strip() if pd.notna(x) and "," in str(x) else np.nan
        )

    # 7. Generate summary statistics
    stats = df.describe(include="all")

    # 8. Save cleaned dataset and statistics report locally
    df.to_csv("cleaned_data.csv", index=False)
    stats.to_csv("summary_stats.csv")
    
    print("\nSuccess! Generated 3 files:")
    print(" - raw_data.csv (original unmodified dataset)")
    print(" - cleaned_data.csv (cleaned dataset)")
    print(" - summary_stats.csv (statistical summary)")

if __name__ == "__main__":
    run_data_pipeline()