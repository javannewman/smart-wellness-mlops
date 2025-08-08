import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "heart_rate": np.random.randint(60, 100, 500),
    "sleep_hours": np.random.uniform(5, 9, 500),
    "steps": np.random.randint(4000, 12000, 500)
}

df = pd.DataFrame(data)
df["wellness_score"] = (0.3 * df["heart_rate"] +
                        0.4 * df["sleep_hours"] +
                        0.3 * df["steps"] / 100).round(2)

df.to_csv("data/wellness_data.csv", index=False)
