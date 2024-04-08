import pandas as pd
import random
from faker import Faker

fake = Faker()

# Definitions
days = ["2024-04-01", "2024-04-02", "2024-04-03", "2024-04-04", "2024-04-05"]
diseases = [("D123", "Diabetes"), ("H234", "High Blood Pressure"), ("C345", "Cancer")]
genders = ["M", "F"]

# For each day
for i, day in enumerate(days):
    # Create a list to hold data
    data = []
    # Create 100 records for each day
    for j in range(1, 101):
        patient_id = f'P{i*100 + j}'
        age = random.randint(30, 70)
        gender = random.choice(genders)
        diagnosis_code, diagnosis_description = random.choice(diseases)
        diagnosis_date = day
        # Append the row to the data list
        data.append([patient_id, age, gender, diagnosis_code, diagnosis_description, diagnosis_date])
    
    # Create a DataFrame and write it to CSV
    df = pd.DataFrame(data, columns=["patient_id", "age", "gender", "diagnosis_code", "diagnosis_description", "diagnosis_date"])
    df.to_csv(f'health_data_{day.replace("-", "")}.csv', index=False)