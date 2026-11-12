import requests

API_KEY = "YOUR_OPENWEATHER_API_KEY"   # Get free key from openweathermap.org
city = input("Enter city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    
    print(f"\nWeather in {city.title()}:")
    print(f"Temperature     : {temp}°C")
    print(f"Feels like      : {feels_like}°C")
    print(f"Humidity        : {humidity}%")
    print(f"Description     : {description.capitalize()}")
else:
    print("City not found or API error.")
