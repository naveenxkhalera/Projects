import requests

# Replace with your actual Weatherstack API key
API_KEY = "652e2bff649d35b2c77072b9fd95a537"

# Define the base URL for Weatherstack API
url = f"https://api.weatherstack.com/current?access_key={ '652e2bff649d35b2c77072b9fd95a537'}"

# Query parameters for the city
querystring = {"query": "New Delhi"}  # You can change the city here

# Make a GET request to fetch the weather data
response = requests.get(url, params=querystring)

# Check if the response is successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()

    # Display the weather data
    if 'current' in weather_data:
        print(f"Weather Data for {querystring['query']}:")

        # Extracting specific data
        temperature = weather_data['current']['temperature']
        feels_like = weather_data['current']['feelslike']
        humidity = weather_data['current']['humidity']
        pressure = weather_data['current']['pressure']
        weather_desc = weather_data['current']['weather_descriptions'][0]
        wind_speed = weather_data['current']['wind_speed']
        
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather Description: {weather_desc}")
        print(f"Wind Speed: {wind_speed} km/h")
    else:
        print("Error: Unable to fetch weather data.")
else:
    print(f"Error: Failed to fetch data from Weatherstack API. Status Code: {response.status_code}")
