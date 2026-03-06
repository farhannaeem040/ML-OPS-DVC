# src/generate_data.py
import pandas as pd
import numpy as np

data = pd.DataFrame({
    "names": [ "Alice", "Bob", "Charlie", "David", "Eve" , "Frank", "Grace", "Heidi", "Ivan", "Judy" ],
    "ages": [ 25, 30, 35, 40, 45, 50, 55, 60, 65, 70 ],
    "cities": [ "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose" ]
})

# if data directory does not exist, create it
import os
if not os.path.exists("data"):
    os.makedirs("data")

data.to_csv("data/raw.csv", index=False)

print("Raw data generated")