import tkinter as tk
import time
import serial
import threading
import continuous_threading
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
from plyer import notification 
from tkinter import *


ser = serial.Serial("com8",9600);
val1=0
index=[]
b=20



def readserial():
    global val1
    
    
    ser_bytes = ser.readline();
    ser_bytes=ser_bytes.decode("utf-8");
    val1=ser_bytes;
    index.append(val1);
    
      

    
    	 



        
    if len(index)==1:
            disp1=tk.Label(root,text=index[0],font=("goudy old style",15,"bold"),fg="black").place(x=550,y=150)
           # if index[0]<="25":
              
    
            # notification.notify(
			       #title="Humidity and temperature sensor",
			       #message="Temperature is high", #25
			       #app_icon="image/bell.ico",
			       #timeout=2
            #)
            #time.sleep(6)
	
    
	   
    elif len(index)==2:
       
        disp2=tk.Label(root,text=index[1],font=("goudy old style",15,"bold"),fg="black").place(x=550,y=250)
     
        if index[0]<"35" and ((index[1]>="30") or (index[1]<"60")):
        
           
             notification.notify(
			       title="temperature is not good and Humidity is normal", #45
			       message="This temperature value causes..Hypothermia.\nThis Humidity maintain your healthy level",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)
        if (index[0]=="36" or index[0]=="37") and ((index[1]>="30") or (index[1]<"60")):
             notification.notify(
			       title="Temperature is normal", #45
			       message="temperature between 36 and 37 is normal\nThis Humidity maintain your healthy level",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)

        if index[0]>"38" and (index[1]>="30" or index[1]<"60"):
                notification.notify(
			       title="temperature is not good and humidity is normal",
                      message= "This temperature causes..Hyperthermia(low fever)\nthis humidity maintain your healthy level",
			       timeout=2
            ) 

        if index[0]>"41" and (index[1]>="30" or index[1]>"60"): 
                notification.notify(
			       title="temperature is not good and Humidity is normal", #45
			       message="This temperature value causes..Hyperpyrexia(High fever).",
			       app_icon="image/bell.ico",
			       timeout=2
            )


        if index[1]<"20" and index[0]>"38":
             notification.notify(
			       title=" temperature is not good and Humidity is unhealthy ", #45
			       message="Humidity is unhealthy..Growing mold and bacteria, Stuffy conditions,Overall discomfort",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)

     



        if index[0]>"38" and index[1]<"25":
              
    
             notification.notify(
			       title="temperature is unhealthy and humidity is also unhealthy", #45
			       message=" temperature causes Hyperthermia and humidity is poor low humidity level",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)

        if index[0]>="38.3" and index[1]<"25":
          notification.notify(
			       title="temperature is unhealthy and humidity is also unhealthy", #45
			       message=" temperature causes Hyperthermia and humidity is poor low humidity level",
			       app_icon="image/bell.ico",
			       timeout=2
            )
          time.sleep(6)
       
       
 

	
    if len(index)==2:
        index.clear();

 

t1=continuous_threading.PeriodicThread(0.5,readserial)  

root =tk.Tk()
image1=ImageTk.PhotoImage(file='image/lapi4.jpg')
bgLabel=tk.Label(root,image=image1)
bgLabel.place(x=0,y=0)

root.title("Predicting Air Pollution in specified city")
name=Label(root,text="Predicting Air quality in specified city",font=("times new roman",30,"bold"),fg="red").place(x=180,y=40)


root.geometry("1350x700+0+0");

temp=tk.Label(root,text='Temperature=',font=("times new roman",15,"bold"),fg="black").place(x=400,y=150);
        
       
hum=tk.Label(root,text='Humidity=',font=("times new roman",15,"bold"),fg="black").place(x=400,y=250);
t1.start()
root.mainloop();
