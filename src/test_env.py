import pandas as pd
import numpy as np

# Create a sample DataFrame matching Kenyan county data structure
data = {
    'County': ['Nairobi', 'Kiambu', 'Nakuru', 'Mombasa'],
    'Financial_Inclusion_Rate': [89.5, 82.1, 78.4, 85.0],
    'Banked_Population': [1250000, 980000, 750000, 820000]
}

df = pd.DataFrame(data)

print("--- Kenya County Data Handling Test ---")
print(df)
print("\nSummary Statistics:")
print(df.describe())