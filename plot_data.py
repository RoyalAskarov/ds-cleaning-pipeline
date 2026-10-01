import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")

# 1. Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

# ---------------------------------------------------------
# Chart 1: Top 10 Most Common Data Science Job Titles
# ---------------------------------------------------------
plt.figure(figsize=(10, 6))
top_jobs = df["Job Title"].value_counts().head(10)
sns.barplot(x=top_jobs.values, y=top_jobs.index, hue=top_jobs.index, palette="mako", legend=False)
plt.title("Top 10 Job Titles in Dataset", fontsize=14, fontweight="bold")
plt.xlabel("Number of Postings")
plt.ylabel("Job Title")
plt.tight_layout()
plt.savefig("top_job_titles.png", dpi=300)
plt.close()
print("Saved chart: top_job_titles.png")

# ---------------------------------------------------------
# Chart 2: Distribution of Company Ratings
# ---------------------------------------------------------
if "Rating" in df.columns:
    plt.figure(figsize=(8, 5))
    # Filter out missing ratings
    valid_ratings = df["Rating"].dropna()
    valid_ratings = valid_ratings[valid_ratings > 0]
    
    sns.histplot(valid_ratings, bins=15, kde=True, color="teal")
    plt.title("Distribution of Company Ratings", fontsize=14, fontweight="bold")
    plt.xlabel("Rating (Out of 5.0)")
    plt.ylabel("Company Count")
    plt.tight_layout()
    plt.savefig("company_ratings_distribution.png", dpi=300)
    plt.close()
    print("Saved chart: company_ratings_distribution.png")

# ---------------------------------------------------------
# Chart 3: Top 10 States for Data Science Postings
# ---------------------------------------------------------
if "job_state" in df.columns:
    plt.figure(figsize=(10, 5))
    top_states = df["job_state"].value_counts().head(10)
    sns.barplot(x=top_states.index, y=top_states.values, hue=top_states.index, palette="viridis", legend=False)
    plt.title("Top 10 States with Most Data Science Jobs", fontsize=14, fontweight="bold")
    plt.xlabel("State Abbreviation")
    plt.ylabel("Number of Postings")
    plt.tight_layout()
    plt.savefig("top_states.png", dpi=300)
    plt.close()
    print("Saved chart: top_states.png")

print("\nAll plots generated successfully!")