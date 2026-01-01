import pandas as pd
import numpy as np
import os
print("Current working directory: ",os.getcwd())
print("List of directories: ",os.listdir())
# Set random seed for reproducibility
np.random.seed(42)

# Fixed data
names = ["Alice", "Bob", "Charlie", "David", "Eva",
         "Frank", "Grace", "Henry", "Ivy", "Jack",
         "Katherine", "Leo", "Mia", "Noah", "Olivia",
         "Peter", "Quinn", "Rachel", "Sam", "Taylor"]

genders = ["F", "M", "M", "M", "F",
           "M", "F", "M", "F", "M",
           "F", "M", "F", "M", "F",
           "M", "F", "F", "M", "F"]

# Random data (controlled by seed)
ages = np.random.randint(22, 50, size=20)
salaries = np.random.randint(60000, 180000, size=20)
cities = np.random.choice(
    ["NY", "LA", "Chicago", "Seattle", "Austin", "Boston"], size=20
)
marital_status = np.random.choice(
    ["Single", "Married", "Divorced"], size=20
)

# Create DataFrame
df = pd.DataFrame(
    {
        "name": names,
        "gender": genders,
        "age": ages,
        "marital_status": marital_status,
        "city": cities,
        "salary": salaries,
    },
    index=[f"{i}" for i in range(1,21)]
)

# Save to CSV
df.to_csv("users_data.csv")

print("CSV file saved as users_data.csv")
