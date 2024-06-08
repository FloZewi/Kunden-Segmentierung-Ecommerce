import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Daten einlesen
data = pd.read_csv('data/customer_data.csv')

# Relevante Features für die Segmentierung auswählen
features = data[['annual_income', 'spending_score']]

# KMeans-Modell erstellen und anpassen
kmeans = KMeans(n_clusters=5)
data['cluster'] = kmeans.fit_predict(features)

# Visualisierung der Cluster
plt.figure(figsize=(10, 6))
sns.scatterplot(x='annual_income', y='spending_score', hue='cluster', data=data, palette='viridis')
plt.title('Kundensegmente basierend auf Einkommen und Ausgabenverhalten')
plt.xlabel('Jahreseinkommen')
plt.ylabel('Ausgabenverhalten')
plt.show()

# Ergebnisse speichern
data.to_csv('data/segmented_customers.csv', index=False)
print("CSV-Datei mit Kundensegmenten wurde erfolgreich erstellt.")
