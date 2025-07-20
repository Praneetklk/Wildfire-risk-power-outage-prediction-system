
# Wildfire Risk & Power Outage Prediction System

This project analyzes wildfire risk and power outage probabilities using weather, infrastructure, and socioeconomic data. It leverages GIS principles, clustering, and Python to help utility companies like DTE Energy assess and respond to high-risk areas.

## Features
- Risk analysis using KMeans clustering
- Integration of weather and infrastructure datasets
- Interactive GUI to visualize risk insights
- GIS-like logic using spatially relevant data

## Datasets
- `weather_sample.csv` – synthetic hourly weather data
- `infrastructure_sample.csv` – synthetic infrastructure data

## Run Instructions

### 1. Risk Analysis Script
```bash
python risk_analysis.py
```

### 2. GUI Application
```bash
python wildfire_gui.py
```

## Requirements
- Python 3.x
- pandas, scikit-learn, matplotlib, tkinter

## Future Enhancements
- Integrate real ArcGIS and shapefile overlays
- Incorporate real-time wildfire alerts or satellite imagery
