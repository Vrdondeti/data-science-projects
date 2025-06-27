
# Weather Lookup App
# Author: Vema Dondeti
# 8/08/2024


# Change Control Log:
# Change#: 1
# Change(s) Made: Initial creation of the weather lookup program.
# Date of Change: 8/08/20024
# Author: Vema Dondeti


"""

Weather Program

This program allows users to look up the current weather by either city name or zip code in the US.
Users can choose between Celsius, Fahrenheit, or Kelvin for temperature units. The program retrieves
weather data from the OpenWeatherMap API and displays it in a formatted manner.

API Key:
The program uses an API key for accessing the OpenWeatherMap service.

"""

import requests
from datetime import datetime
import textwrap

# API Key for OpenWeatherMap
API_KEY = 'Insert Your API Key Here'


# Class to manage weather data retrieval and display using OpenWeatherMap API.
class WeatherProgram:

    # Initialize WeatherProgram with API key and default values.
    def __init__(self, api_key):
        self.api_key = api_key
        self.latitude = None
        self.longitude = None
        self.city = None
        self.zip_code = None
        self.state = None
        self.temp_unit = None

    #  Get User's choice of weather lookup method or quit option.
    @staticmethod
    def get_user_choice():
        print("\nHow would you like to look up the weather today?")
        print("1 - By City")
        print("2 - By Zip code")
        print("q - Quit")
        choice = input("Enter your choice: ")
        return choice

    # get city and state for weather lookup by city
    def set_city(self):

        while True:
            self.city = input("\nEnter city name: ").strip()
            self.state = input("Enter state abbreviation (e.g., 'TX'): ").strip().upper()

            if self.city and self.state:
                break
            else:
                print("\n***Error: Both city name and state abbreviation are required. Please try again.***")

    # set zip code for weather lookup by zip
    def set_zip_code(self):

        self.zip_code = self.get_zip_code()

    # get a valid 5 digit zip code for the lookup
    def get_zip_code(self):
        while True:
            self.zip_code = input("\nEnter a zip code (5 digits): ").strip()

            if self.zip_code.isdigit():
                if len(self.zip_code) > 5:
                    print("\n***Error: Zip code cannot be more than 5 digits. Please try again.***")
                else:
                    self.zip_code = self.zip_code.zfill(5)
                    return self.zip_code
            else:
                print("\n***Error: Zip code must contain only digits. Please try again.***")

    # get temperature unit for API request ('metric', 'imperial', or 'standard').
    def set_temperature_unit(self):
        while True:
            unit_choice = input(
                "\nPlease enter the temperature unit you prefer:\n"
                "(C) for Celsius\n"
                "(F) for Fahrenheit\n"
                "(K) for Kelvin\n"
                "Enter your choice (C, F, or K): "
            ).lower()
            if unit_choice == 'c':
                self.temp_unit = 'metric'
                break
            elif unit_choice == 'f':
                self.temp_unit = 'imperial'
                break
            elif unit_choice == 'k':
                self.temp_unit = 'standard'
                break
            else:
                print("\n***Invalid choice. Please enter 'C', 'F', or 'K'.***")

    # fetch geo coordinates based on city or zip code.
    def get_geo_coordinates(self):

        base_url = 'http://api.openweathermap.org/geo/1.0/'

        if self.city and self.state:
            complete_url = f"{base_url}direct?q={self.city},{self.state},US&limit=1&appid={self.api_key}"
        elif self.zip_code:
            complete_url = f"{base_url}zip?zip={self.zip_code},US&appid={self.api_key}"
        else:
            print("\n***Error: Must provide either city or zip code.***")
            return None

        try:
            # Send a GET request to the API endpoint with the complete URL
            response = requests.get(complete_url)

            # Raise an HTTPError for bad responses
            response.raise_for_status()

            # Parse the JSON response from the API into a Python dictionary
            response_dict = response.json()

            # If the response is empty or contains no data, return None
            if not response_dict:
                return None

            # Extract latitude and longitude from the response.
            # The response is a list for city lookups and a dictionary for zip code lookups.
            # The following line ensures that 'location' is always a dictionary with the relevant location details.
            location = response_dict[0] if isinstance(response_dict, list) else response_dict

            self.latitude = location['lat']
            self.longitude = location['lon']

            return self.latitude, self.longitude

        except requests.exceptions.ConnectionError as conn_err:
            error_message = f"\nUnable to connect to the server: {conn_err}"
            print(textwrap.fill(error_message, width=80))
            return None

        except requests.exceptions.Timeout as timeout_err:
            error_message = f"\nRequest timed out. Please try again later: {timeout_err}"
            print(textwrap.fill(error_message, width=80))
            return None

        except requests.exceptions.HTTPError as http_err:
            error_message = f"\nAn HTTP error occurred: {http_err}"
            print(textwrap.fill(error_message, width=80))
            return None

        except requests.exceptions.RequestException as req_err:
            error_message = f"\nFailed to retrieve location coordinates: {req_err}"
            print(textwrap.fill(error_message, width=80))
            return None

    # Fetch weather data using the current latitude and longitude.
    def get_weather(self):
        base_url = 'https://api.openweathermap.org/data/2.5/weather?'

        if self.latitude is None or self.longitude is None:
            print(
                "***Error: Coordinates must be set before fetching weather.***\n"
                "***Please ensure you have entered a valid city name and state or a valid zip code.***"
            )
            return None

        complete_url = (
            f"{base_url}lat={self.latitude}&lon={self.longitude}"
            f"&units={self.temp_unit}&appid={self.api_key}"
        )

        try:
            # Send a GET request to the API endpoint with the complete URL
            response = requests.get(complete_url)

            # Raise an HTTPError for bad responses
            response.raise_for_status()

            # Parse the JSON response from the API into a Python dictionary
            weather_data = response.json()

            # Return the parsed weather data
            return weather_data

        except requests.exceptions.ConnectionError as conn_err:
            error_message = f"\nUnable to connect to the server: {conn_err}"
            print(textwrap.fill(error_message, width=80))
            return None

        except requests.exceptions.Timeout as timeout_err:
            error_message = f"\nRequest timed out. Please try again later: {timeout_err}"
            print(textwrap.fill(error_message, width=80))
            return None

        except requests.exceptions.HTTPError as http_err:
            error_message = f"\nAn HTTP error occurred: {http_err}"
            print(textwrap.fill(error_message, width=80))
            return None

        except requests.exceptions.RequestException as req_err:
            error_message = f"\nFailed to retrieve weather data: {req_err}"
            print(textwrap.fill(error_message, width=80))
            return None

    # Display the weather data in a formatted manner.
    def display_weather(self, weather_data):

        # Determine the unit label based on the user's choice
        unit_label = {
            'metric': '°C',
            'imperial': '°F',
            'standard': 'K'
        }.get(self.temp_unit, 'Unknown')

        # Extract main weather details from the API response
        main_weather = weather_data['main']
        weather_desc = weather_data['weather'][0]['description']

        # Retrieve specific weather attributes
        current_temp = main_weather['temp']
        feels_like = main_weather['feels_like']
        low_temp = main_weather['temp_min']
        high_temp = main_weather['temp_max']
        pressure = main_weather['pressure']
        humidity = main_weather['humidity']

        # Start with the city name from the weather data
        location = f"{weather_data['name']}"

        # Append state abbreviation city look up
        if self.state:
            location += f", {self.state}"
        # Append zip code if weather lookup is by zip code
        elif self.zip_code:
            location += f", {self.zip_code}"

        print("\n" + "-" * 50)  # Line at the top
        print(
            f"Weather for {location}"
            f" at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print("" + "-" * 50)
        print(f"{'Current Temp:':<20} {current_temp} {unit_label}")
        print(f"{'Feels Like:':<20} {feels_like} {unit_label}")
        print(f"{'Low Temp:':<20} {low_temp} {unit_label}")
        print(f"{'High Temp:':<20} {high_temp} {unit_label}")
        print(f"{'Pressure:':<20} {pressure} hPa")
        print(f"{'Humidity:':<20} {humidity}%")
        print(f"{'Weather Description:':<20} {weather_desc.capitalize()}")
        print("-" * 50)  # Line at the bottom


# Main function to run the weather lookup program.
def main():

    print("\nWelcome to the Weather Program!")
    print("This weather_app allows you to lookup the current weather by city or zip code in the US.")

    while True:

        weather_app = WeatherProgram(API_KEY)

        choice = weather_app.get_user_choice()

        if choice.lower() == 'q':
            print("\nThank you for using the Weather Program. Have a nice day!")
            break

        if choice == '1':
            weather_app.set_city()
            coordinates = weather_app.get_geo_coordinates()

        elif choice == '2':
            weather_app.set_zip_code()
            coordinates = weather_app.get_geo_coordinates()
        else:
            print("\n***Invalid choice. Please enter '1' for city lookup or '2' for zip code lookup.***")
            continue

        if not coordinates:
            print(
                "\n***Unable to retrieve geo coordinates. Please ensure that valid "
                "city/state or zip code details are entered and try again.***"
            )
            continue

        # Set the temperature unit
        weather_app.set_temperature_unit()

        # Fetch and display weather data
        weather_data = weather_app.get_weather()

        # If weather data is successfully retrieved, display the weather information
        if weather_data:
            weather_app.display_weather(weather_data)


if __name__ == "__main__":
    main()
