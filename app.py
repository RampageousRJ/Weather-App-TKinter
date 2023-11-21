from tkinter import *
from tkinter import messagebox,END
import datetime as dt
import requests
from dotenv import load_dotenv
import os
load_dotenv()

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry('650x500')
        self.minsize(500,500)
        self.maxsize(1500,1500)
        self.grid()
        self.create_widgets()
         
    def clearText(self):
        self.location_text.delete("1.0","end")
        
    def printMessage(self):
        CITY = self.location_text.get("1.0",END).strip('\n')
        url = os.getenv('BASE_URL') + "appid=" + os.getenv("API_KEY") + "&q=" + CITY
        response = requests.get(url).json()
        print(response['main']['temp'])
    
    def create_widgets(self):
        self.location_text = Text(self,bg='light cyan')
        self.location_text.grid(row=0,column=0,columnspan=2,sticky='nsew')
        self.button1 = Button(self,text='Clear',command=self.clearText,background='grey').grid(row=1,column=0,sticky='nsew')
        self.button2 = Button(self,text='Submit',command=self.printMessage,background='grey').grid(row=1,column=1,sticky='nsew')

if __name__=='__main__':
    app = App()
    app.mainloop()