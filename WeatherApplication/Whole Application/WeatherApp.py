from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests


url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
#config_file = 'config.ini'
#config = ConfigParser()
#config.read(config_file)
key_api = '2fe0951838093c3a4d96c41626294ac8'


def get_weather(city):
    result = requests.get(url.format(city, key_api))
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']['country']
        temperature_kelvin = json['main']['temp']
        temperature_celsius = temperature_kelvin - 272.15
        temperature_fahrenheit = temperature_celsius * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = [city, country, temperature_celsius, temperature_fahrenheit, icon, weather]
        return final
    else:
        return None


def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_label['text'] = '{}, {}'.format(weather[0], weather[1])
        #image['bitmap'] = 'images_icons/{}.png'.format(weather[4])
        temperature_label['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_label['text'] = weather[5]
    else:
        messagebox.showerror('Error', 'No City Found: {}'.format(city))


app = Tk()
app.title("Weather Application")
app.geometry('700x350')

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_button = Button(app, text='Search Weather', width=12, command=search)
search_button.pack()

location_label = Label(app, text='', font=('bold', 20))
location_label.pack()

image = Label(app, bitmap='')
image.pack()

temperature_label = Label(app, text='')
temperature_label.pack()

weather_label = Label(app, text='')
weather_label.pack()

app.mainloop()