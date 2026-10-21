import pandas as pd

# Load our Kenya county dataset
data = {
    'County': ['Nairobi', 'Kiambu', 'Nakuru', 'Mombasa', 'Kisumu', 'Eldoret'],
    'Region': ['Central', 'Central', 'Rift Valley', 'Coast', 'Nyanza', 'Rift Valley'],
    'Financial_Inclusion_Rate': [89.5, 82.1, 78.4, 85.0, 76.2, 79.1],
    'Banked_Population': [1250000, 980000, 750000, 820000, 610000, 680000]
}
df = pd.DataFrame(data)

# 1. Filtering: Counties with Financial Inclusion > 80%
high_inclusion = df[df['Financial_Inclusion_Rate'] > 80.0]
print("--- Counties with > 80% Financial Inclusion ---")
print(high_inclusion[['County', 'Financial_Inclusion_Rate']])

# 2. Grouping: Average Banked Population by Region
region_grouped = df.groupby('Region')['Banked_Population'].mean().reset_index()
print("\n--- Average Banked Population by Region ---")
print(region_grouped)