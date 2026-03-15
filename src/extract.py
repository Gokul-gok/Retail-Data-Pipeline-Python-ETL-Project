import pandas as pd
import os

# Extract function is already implemented for you 
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on = "index")
    return merged_df

# Call the extract() function and store it as the "merged_df" variable
merged_df = extract(grocery_sales, "data/raw/extra_data.parquet")
print(merged_df.info())
