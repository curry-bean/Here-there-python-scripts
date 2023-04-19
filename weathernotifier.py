#importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

#creating the window
wn = Tk()
wn.title("PythonGeeks Weather Alert")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19',bg='azure').place(x=100,y=15)

#Getting the city name 
Label(wn, text='Enter the Location:', font=("Courier", 13),bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

#Button to get notification
btn = Button(wn, text='Get Notification', font=7, fg='grey19',command=getNotification()).place(relx=0.4, rely=0.75)
#run the window till the closed by user
wn.mainloop()

#Function to get notification of weather report
def getNotification():
    cityName=place.get() #getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?" #base url from where we extract weather report
    try:
        # This is the complete url to get weather conditions of a city
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(complete_url) #requesting for the the content of the url
        x = response.json() #converting it into json 
        y = x["main"] #getting the "main" key from the json object
 
        # getting the "temp" key of y
        temp = y["temp"]
        temp-=273 #converting temperature from kelvin to celsius

        # storing the value of the "pressure" key of y
        pres = y["pressure"]

        # getting the value of the "humidity" key of y
        hum = y["humidity"]

        # storing the value of "weather" key in variable z
        z = x["weather"]

        # getting the corresponding "description"
        weather_desc = z[0]["description"]

        # combining the above values as a string 
        info="Here is the eather description of "+ cityName+ ":"+" \nTemperature = " +str(temp) +"°C"+"\n atmospheric pressure = " + str(pres) + "hPa"+"\n humidity = " +str(hum) +"%"+"\n description of the weather= " + str(weather_desc)

        #showing the notification 
        notification.notify(
                    title = "YOUR WEATHER REPORT",
                    message=info ,

                    # displaying time
                    timeout=2)
        # waiting time
        time.sleep(7)
    
    except Exception as e:
        mb.showerror('Error',e)#show pop up message if any error occurred