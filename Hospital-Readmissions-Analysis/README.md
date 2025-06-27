# Healthcare Readmissions and Environmental Factors Analysis

## Project Overview

This project investigates the relationship between healthcare readmission rates and environmental and demographic factors across the United States—specifically humidity, air quality, and population density. The objective is to explore whether non-clinical external conditions may show associations with hospital readmission trends.

Using data from three distinct sources—including an API, a flat file, and a web dataset—I merged them into an SQLite database, performed SQL joins, and developed visualizations to identify potential patterns. The project highlights the importance of thoughtful data integration, proper cleaning, and ethical analysis when working with health-related data.

## Data Sources

1. **Healthcare Readmissions and Mortality Data**  
   Source: [Kaggle – U.S. Healthcare Readmissions and Mortality](https://www.kaggle.com/datasets/thedevastator/us-healthcare-readmissions-and-mortality)  
   Format: Flat file (CSV)  
   Description: Contains hospital-level scores for mortality and readmission across multiple conditions.

2. **State Population Density Data**  
   Source: [States101 – Population Data](https://www.states101.com/populations)  
   Format: Web dataset (HTML table extracted as CSV)  
   Description: Provides population density and demographic details by U.S. state.

3. **Environmental Data (Humidity & Weather)**  
   Source: [OpenWeatherMap API](https://openweathermap.org/api)  
   Format: API (JSON)  
   Description: Supplies historical and current weather conditions, including humidity, by location.

## Tools & Skills Used

- **Languages:** Python (Pandas, Requests, SQLite3, Seaborn, Matplotlib)
- **Data Storage:** SQLite (relational joins across multiple sources)
- **Environment:** Jupyter Notebook
- **Skills Applied:**  
  - Multi-source data cleaning and integration  
  - Relational database design and SQL querying  
  - Exploratory Data Analysis (EDA) and visualization  
  - Ethical interpretation of observational health data

## Highlights

- Combined environmental, demographic, and hospital datasets into a unified database for cross-analysis.
- Created visualizations to explore potential associations between hospital readmission rates and external variables like air quality or population density.
- Emphasized correlation analysis without implying causation, ensuring clarity and responsibility in interpretation.
- Focused on reproducibility, transparency, and ethical data use throughout the process.

## Summary

This project demonstrates how data from different domains can be merged to provide insights into public health trends. It showcases practical data engineering, thoughtful analysis, and responsible storytelling—all essential for ethical and effective data science in healthcare.