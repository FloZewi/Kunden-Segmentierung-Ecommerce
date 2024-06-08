import pandas as pd
import random
import os


# Funktion zum Generieren zufälliger Kundendaten
def generate_random_customer_data(num_records):
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Daisy', 'Edward', 'Fiona']
    last_names = ['Doe', 'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller']
    categories = ['Electronics', 'Fashion', 'Home', 'Books', 'Toys']

    data = []

    for _ in range(num_records):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(18, 70)
        annual_income = random.randint(20000, 150000)
        spending_score = random.randint(1, 100)
        favorite_category = random.choice(categories)
        data.append([first_name, last_name, age, annual_income, spending_score, favorite_category])

    return pd.DataFrame(data, columns=['first_name', 'last_name', 'age', 'annual_income', 'spending_score', 'favorite_category'])


# Anzahl der zu generierenden Datensätze
num_records = 500

# Generieren der Daten
customer_data = generate_random_customer_data(num_records)

# Verzeichnis erstellen, falls es nicht existiert
os.makedirs('data', exist_ok=True)

# Speichern der Daten als CSV-Datei
customer_data.to_csv('data/customer_data.csv', index=False)

print("CSV-Datei mit Kundendaten wurde erfolgreich erstellt.")
