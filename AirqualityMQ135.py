import tkinter as tk
import time
import serial
import threading
import continuous_threading
from plyer import notification 
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import *

ser = serial.Serial("com8",9600);
val1=0
index=[]


    
def readserial():
        global val1
    
        ser_bytes = ser.readline();
        ser_bytes=ser_bytes.decode("utf-8");
        val1=ser_bytes;
        index.append(val1);

        if len(index)==1:
         disp1=Label(root,text=index[0],font=("times new roman",15,"bold")).place(x=540,y=200)
         if index[0]>="50" :
             notification.notify(
			       title="Air Quality  sensor", #0 to 50 good
			       message="Air Quality is normal",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)
	     
         if index[0]>="51" and index[0]<="100":
             notification.notify(
			       title="Air Quality is moderate", #0 to 50 good
			       message="..Unusually sensitive individuals should consider limiting prolonged outdoor exerction",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)

         if index[0]>="101" and index[0]<="150":
             notification.notify(
			       title="Air Quality is unhealthy for sensitive groups.", #0 to 50 good
			       message="..Children active adults,and peoples with respiratory disease,such as asthma,should avoid prolonged outdoor exertion;everyone else should limit prolonged outdoor exertion",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)

         while index[0]>="151":
             notification.notify(
			       title="Air Quality is Unhealthy", #0 to 50 good
			       message="Children active adults,and peoples with respiratory disease,such as asthma,should avoid prolonged outdoor exertion;everyone else should limit prolonged outdoor exertion",
			       app_icon="image/bell.ico",
			       timeout=2
            )
             time.sleep(6)
	
         
	
    	
        
	
    
    
t1=continuous_threading.PeriodicThread(0.5,readserial) 

root =tk.Tk()
image1=ImageTk.PhotoImage(file='image/lapi4.jpg')
bgLabel=tk.Label(root,image=image1)
bgLabel.place(x=0,y=0)
name=Label(root,text="Predicting Air quality in specified city",font=("times new roman",30,"bold"),fg="red").place(x=130,y=40)

root.title("Predicting Air Pollution in specified city")


root.geometry("1350x700+0+0");

temp=tk.Label(root,text='Air Quality=',font=("times new roman",15,"bold")).place(x=400,y=200);
        
       

t1.start()
root.mainloop();
    



        

