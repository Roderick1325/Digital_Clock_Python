from tkinter import *
import time
root=Tk()
root.title("DIGITAL CLOCK")
root.geometry("609x320+0+0")
root.config(bg="#0f3460")

def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    #print(h,m,s)
    if int(h)>12 and int(m)>0:
        lbl_noon.config(text="PM")
    if int(h)>12:
        h = str(int(h)-12)
    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)
    lbl_noon.after(200,clock)

#<-------------- Hora ----------------->
lbl_hr=Label(root,text="12", font=("Arial", 25,"bold"), bg="#0278ae", fg="white")
lbl_hr.place(x=19,y=26, width=120, height=160)
#<-------------- Texto hora ----------------->
lbl_hr1=Label(root,text="Hours", font=("Arial", 25,"bold"), bg="#0278ae", fg="white")
lbl_hr1.place(x=19,y=213, width=122, height=53)
#<-------------- Minutos ----------------->
lbl_min=Label(root,text="00", font=("Arial", 25,"bold"), bg="#51adcf", fg="white")
lbl_min.place(x=162,y=26, width=120, height=160)
#<-------------- Texto Minutos ----------------->
lbl_min1=Label(root,text="Minutes", font=("Arial", 25,"bold"), bg="#51adcf", fg="white")
lbl_min1.place(x=162,y=213, width=122, height=53)
#<-------------- Seconds ----------------->
lbl_sec=Label(root,text="00", font=("Arial", 25,"bold"), bg="#ff4646", fg="white")
lbl_sec.place(x=305,y=26, width=120, height=160)
#<-------------- Texto Seconds ----------------->
lbl_sec1=Label(root,text="Seconds", font=("Arial", 25,"bold"), bg="#ff4646", fg="white")
lbl_sec1.place(x=305,y=213, width=122, height=53)
#<-------------- Noon ----------------->
lbl_noon=Label(root,text="00", font=("Arial", 25,"bold"), bg="#ff4646", fg="white")
lbl_noon.place(x=448,y=26, width=120, height=160)
#<-------------- Texto Noon ----------------->
lbl_noon1=Label(root,text="Seconds", font=("Arial", 25,"bold"), bg="#ff4646", fg="white")
lbl_noon1.place(x=448,y=213, width=122, height=53)

clock()
root.mainloop()