from tkinter import *
from tkinter import messagebox,END
import datetime as dt
import requests
from dotenv import load_dotenv
import os
load_dotenv()

def convertTemp(kelvin):
    return str(round(kelvin-273.15,2))+" °C"

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry('400x250')
        self.maxsize(650,500)
        self.grid()
        self.create_widgets()
         
    def clearText(self):
        self.location_text.delete("1.0","end")
         
    def checkWeather(self):
        CITY = self.location_text.get("1.0",END).strip('\n')
        url = os.getenv('BASE_URL') + "appid=" + os.getenv("API_KEY") + "&q=" + CITY
        response = requests.get(url).json()
        current_temp = response['main']['temp']
        max_temp = response['main']['temp_max']
        min_temp = response['main']['temp_min']
        feels_like = response['main']['feels_like']
        humidity = response['main']['humidity']
        messagebox.showinfo(title=f"{CITY} Weather\n",message=f'WEATHER DETAILS\nTemperature: {convertTemp(current_temp)}\nMaximum Temperature: {convertTemp(max_temp)}\nMinimum Temperature: {convertTemp(min_temp)}\nFeels Like: {convertTemp(feels_like)}\nHumidity: {humidity}%')
    
    def create_widgets(self):
        self.location_label = Label(self,text="Enter City Name: ",font=("Monocraft",10)).grid(row=0,column=0,pady=(40,5),padx=(60,0))
        self.location_text = Text(self,bg='light cyan',width=30,height=5)
        self.location_text.grid(row=1,column=0,columnspan=2,pady=(0,20),padx=(60,0),sticky="nsew")
        self.button2 = Button(self,text='Submit',command=self.checkWeather,background='grey',width=15).grid(row=2,column=0,sticky="nsew",padx=(60,0))
        self.button1 = Button(self,text='Clear',command=self.clearText,background='grey',width=5).grid(row=2,column=1,sticky="nsew",padx=(60,0))

if __name__=='__main__':
    app = App()
    app.mainloop()