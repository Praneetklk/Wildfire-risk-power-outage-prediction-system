# Wildfire-risk-power-outage-prediction-system
This project analyzes wildfire risk and power outage probabilities using weather, infrastructure, and socioeconomic data. It leverages GIS principles, clustering, and Python to help utility companies like DTE Energy assess and respond to high-risk areas.

## Features
- Risk analysis using KMeans clustering
- Integration of weather and infrastructure datasets
- Interactive GUI to visualize risk insights
- GIS-like logic using spatially relevant data

## Datasets
- Full links to datasets can be found here

-Wildfire dataset
https://apps.fs.usda.gov/fsgisx03/rest/services/wo_spf_fam/Nat_BurnProbability/ImageServer
https://data-usfs.hub.arcgis.com/datasets/7cea729c213e409aade5a2838293f09e/about

-Weather dataset
https://www.weather.gov/fire/
https://www.utilitydive.com/spons/integrating-advanced-weather-data-with-utility-asset-outage-analysis-to-qua/652592/

Powergrid dataset 
https://resilience.climate.gov/datasets/fedmaps::u-s-electric-power-transmission-lines/explore

- `weather_sample.csv` – synthetic hourly weather data
- `infrastructure_sample.csv` – synthetic infrastructure data

## Run Instructions

### 1. Risk Analysis Script

python risk_analysis.py


### 2. GUI Application

python wildfire_gui.py 


## Requirements
- Python 3.x
- pandas, scikit-learn, matplotlib, tkinter
- ArcGIS Pro

## Future Enhancements
- Integrate real ArcGIS and shapefile overlays
- Incorporate real-time wildfire alerts or satellite imagery
