import requests

api_key = '2fe0951838093c3a4d96c41626294ac8'

users_input = input("Enter City: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={users_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    coord_lon = weather_data.json()['coord']['lon']
    coord_lat = weather_data.json()['coord']['lat']
    weather = weather_data.json()['weather'][0]['main']
    weather_overcast = weather_data.json()['weather'][0]['description']
    temperature = round(weather_data.json()['main']['temp'])

    print(f"The weather in {users_input} (Coordinates: {coord_lon} / {coord_lat})  is: {weather}")
    print(f"Overcast in {users_input} is: {weather_overcast}")
    print(f"The temperature in {users_input} is: {temperature:.2f} fahrenheit or {(temperature-32)/1.8:.2f} Celsius")


