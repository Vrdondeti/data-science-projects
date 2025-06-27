# Interactive Weather Lookup App (OpenWeatherMap API)

## Project Overview

This Python application provides real-time weather updates by integrating with the OpenWeatherMap API. Users can choose to enter either a city/state or ZIP code and receive a detailed, readable weather information. The application supports temperature units in Celsius, Fahrenheit, and Kelvin.

The project focuses on clean code structure, modular design, and robust error handling. It’s designed to demonstrate effective API consumption, user interaction, and Python best practices.

## Key Features

- Supports city/state and ZIP code weather lookups
- Performs GEO lookup followed by weather forecast retrieval using latitude and longitude
- Allows users to choose temperature units: Celsius, Fahrenheit, or Kelvin
- Displays:
  - Location (city/state)
  - Current temperature and "feels like"
  - High and low temperatures
  - Humidity, pressure, and weather description
- Handles invalid input gracefully with input validation
- Uses try-except blocks for network error handling and clean user feedback

## Technologies Used

- Python 3
- OpenWeatherMap API
- `requests` library
- Clean function-based structure following PEP8
