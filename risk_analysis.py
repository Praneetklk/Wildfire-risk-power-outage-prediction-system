
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load datasets
weather_df = pd.read_csv("data/weather_sample.csv")
infra_df = pd.read_csv("data/infrastructure_sample.csv")

# Merge datasets
merged_df = pd.concat([weather_df.reset_index(drop=True), infra_df.reset_index(drop=True)], axis=1)

# Feature selection
features = merged_df[['temperature', 'humidity', 'wind_speed', 'precipitation',
                      'distance_to_grid', 'population_density', 'power_line_age']]

# Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
merged_df['risk_cluster'] = kmeans.fit_predict(features)

# Display results
print(merged_df[['temperature', 'humidity', 'distance_to_grid', 'risk_cluster']].head())

# Plot results
plt.figure(figsize=(10, 6))
scatter = plt.scatter(merged_df['temperature'], merged_df['humidity'],
                      c=merged_df['risk_cluster'], cmap='viridis')
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Wildfire Risk Clustering")
plt.colorbar(scatter, label='Cluster')
plt.grid(True)
plt.show()
