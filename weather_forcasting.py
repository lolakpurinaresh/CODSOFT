from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk

root=Tk()
root.title("WEATHER FORCAST")
root.geometry("1000x500+300+200")
root.resizable(0,0)

def getWeather():
    city=main_text.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude)}°N,{round(location.longitude)}°E")

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    timezone.config(text="Current weather")

    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e7a5241f83b7d67fd8c1a00ede02d983"


    online_data=requests.get(api).json()
    condition=online_data["weather"][0]["main"]
    description=online_data["weather"][0]["description"]
    temp=int(online_data['main']['temp']-273.15)
    pressure=online_data['main']['pressure']
    humidity=online_data['main']['humidity']
    wind=online_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"//","FEELS","LIKE","//"))


    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)






##SEARCH BOX
search_image=PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\search.png")
my_image=Label(image=search_image)
my_image.place(x=150,y=20)

main_text=tk.Entry(root,justify="center",width=30,font=("times new roman","15","bold"))
main_text.place(x=165,y=40)
main_text.focus()

##SEARCH ICON

search_icon=PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\searchicon.png")
image_icon=Button(image=search_icon,command=getWeather)
image_icon.place(x=450,y=20)

##BOX IMAGE
BOX_image=PhotoImage(file=r"C:\Users\Admin\OneDrive\Desktop\skybox.png")
mybox_image=Label(image=BOX_image)
mybox_image.pack(padx=3,pady=8,side=BOTTOM)

##LABELS

label1=Label(root,text="WIND",font=("Calibri","15","bold"),bg="black",fg="white")
label1.place(x=200,y=375)

label2=Label(root,text="HUMIDITY",font=("Calibri","15","bold"),bg="black",fg="white")
label2.place(x=340,y=375)

label3=Label(root,text="DESCRIPTION",font=("Calibri","15","bold"),bg="black",fg="white")
label3.place(x=510,y=375)

label4=Label(root,text="PRESSURE",font=("Calibri","15","bold"),bg="black",fg="white")
label4.place(x=680,y=375)

t=Label(font=("arial","70","bold"))
t.place(x=350,y=200)
c=Label(font=("arial","15","bold"))
c.place(x=350,y=180)


w=Label(text="---",font=("arial","15","bold"),bg="Black",fg="white")
w.place(x=210,y=430)

h=Label(text="---",font=("arial","15","bold"),bg="Black",fg="white")
h.place(x=370,y=430)

d=Label(text="---",font=("arial","15","bold"),bg="Black",fg="white")
d.place(x=530,y=430)

p=Label(text="---",font=("arial","15","bold"),bg="Black",fg="white")
p.place(x=710,y=430)

clock=Label(root,font=("arial","10","bold"),fg='blue',bg="white")
clock.place(x=350,y=125)

timezone=Label(root,font=("arial","10","bold"),fg='white',bg="Black")
timezone.place(x=350,y=100)

long_lat=Label(root,font=("arial","10","bold"),fg='white',bg="red")
long_lat.place(x=350,y=160)

root.mainloop()
