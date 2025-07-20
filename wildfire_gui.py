
import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.cluster import KMeans

def predict_risk():
    try:
        weather_df = pd.read_csv("data/weather_sample.csv")
        infra_df = pd.read_csv("data/infrastructure_sample.csv")
        merged_df = pd.concat([weather_df.reset_index(drop=True), infra_df.reset_index(drop=True)], axis=1)
        features = merged_df[['temperature', 'humidity', 'wind_speed', 'precipitation',
                              'distance_to_grid', 'population_density', 'power_line_age']]
        kmeans = KMeans(n_clusters=3, random_state=42)
        merged_df['risk_cluster'] = kmeans.fit_predict(features)

        high_risk_locations = merged_df[merged_df['risk_cluster'] == merged_df['risk_cluster'].max()]
        msg = f"High Risk Zone Count: {len(high_risk_locations)}\n"
        msg += f"Average Temp: {high_risk_locations['temperature'].mean():.2f}°F"
        messagebox.showinfo("Risk Prediction", msg)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process data: {e}")

root = tk.Tk()
root.title("Wildfire & Power Outage Risk GUI")
root.geometry("400x200")

label = tk.Label(root, text="Wildfire Risk Prediction", font=("Helvetica", 16))
label.pack(pady=20)

btn = tk.Button(root, text="Run Risk Prediction", command=predict_risk, font=("Helvetica", 12), bg="orange")
btn.pack(pady=10)

root.mainloop()
