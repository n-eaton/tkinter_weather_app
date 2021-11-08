import tkinter as tk
import os
import requests
from datetime import datetime



def getWeather(canvas):
    city_name = textfield.get()
    password = os.environ['weather_app_password']
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={password}"
    data = requests.get(api).json()

    condition = data['weather'][0]['main']
    temp_c = int((data["main"]["temp"])-273.15)
    temp_f = int(((data["main"]["temp"])-273.15)*1.8+32)
    description= data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']
    time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    final_info = "\n"+condition+ "\n" + str(temp_c)+ "°C   or   "+str(temp_f)+"°F"+"\n"


    final = "\n"+"Currently   "+description+"\n"+"Humidity   "+ str(humidity)+'%'+"\n"+"Wind   "+str(wind)+ "kmph"+"\n"+"\n"+str(time)


    l1.config(text = final_info)
    l2.config(text = final)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather Forecast")

f = ("poppins", 15,"bold")
t = ("poppins", 35,"bold")


textfield = tk.Entry(canvas,justify="center", font=t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

l1 = tk.Label(canvas, font=t)
l1.pack()

l2 = tk.Label(canvas, font=f)
l2.pack()

canvas.mainloop()
