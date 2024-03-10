import customtkinter as ctk
from customtkinter import filedialog
import pyglet
from main import * 
import threading
import time


pyglet.font.add_file('league.ttf')

ctk.set_appearance_mode("light")

ctk.set_default_color_theme("green")


class TrafficLight():
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.state = 0
        self.canvas = ctk.CTkCanvas(self.root,width=50, height=150) 
        self.canvas.place(x=self.x, y=self.y)
        self.red_light = self.canvas.create_oval(10,10,40,40,fill="black")
        self.yellow_light = self.canvas.create_oval(10,60,40,90,fill="black")
        self.green_light = self.canvas.create_oval(10,110,40,140,fill="black")
    
    def change_state(self,s):
        self.state = s
        if self.state == 0:
            self.canvas.itemconfigure(self.red_light,fill="red")
            self.canvas.itemconfigure(self.yellow_light,fill="black")
            self.canvas.itemconfigure(self.green_light,fill="black")
        elif self.state == 1:
            self.canvas.itemconfigure(self.red_light, fill="black")
            self.canvas.itemconfigure(self.yellow_light, fill="yellow")
            self.canvas.itemconfigure(self.green_light, fill="black")   
        elif self.state == 2:
            self.canvas.itemconfigure(self.red_light, fill="black")
            self.canvas.itemconfigure(self.yellow_light, fill="black")
            self.canvas.itemconfigure(self.green_light, fill="green")






            

    
app = ctk.CTk()
app.title("TraffAI")
app.geometry("900x900")

video_array = []

def select_video1():
    video1 = filedialog.askopenfilename(title="Select a file")
    video_array.append(video1)
def select_video2():
    video2 = filedialog.askopenfilename(title="Select a file")
    video_array.append(video2)
def select_video3():
    video3 = filedialog.askopenfilename(title="Select a file")
    video_array.append(video3)
def select_video4():
    video4 = filedialog.askopenfilename(title="Select a file")
    video_array.append(video4)


def countdownOne(root,lane1,lane2,lane3,lane4,seconds,cars):
    startLaneOne(root,lane1,lane2,lane3,lane4)
    textlabel = ctk.CTkLabel(root,text="00:{}".format(seconds),font=("League Spartan",20))
    textlabel.place(x=100,y=100)
    def update_timer():
        nonlocal seconds
        seconds -= 1
        if seconds <= 0:
            startLaneTwo(root,lane1,lane2,lane3,lane4)
            secondsTwo = int((cars[1] / 2) + 5)
            countdownTwo(root,lane1,lane2,lane3,lane4,secondsTwo,cars)
        else:
            textlabel.configure(text="00:{}".format(seconds))
            root.after(1000,update_timer)
    
    update_timer()

def countdownTwo(root,lane1,lane2,lane3,lane4,seconds,cars):
    textlabel = ctk.CTkLabel(root,text="00:{}".format(seconds),font=("League Spartan",20))
    textlabel.place(x=100,y=100)
    def update_time():
        nonlocal seconds
        seconds -= 1
        if seconds <= 0:
            startLaneThree(root,lane1,lane2,lane3,lane4)
            secondsThree = int((cars[2]/2) + 5)
            countdownThree(root,lane1,lane2,lane3,lane4,secondsThree)
        else:
            textlabel.configure(text="00:{}".format(seconds))
            root.after(1000,update_time)
    
    update_time()

def countdownThree(root,lane1,lane2,lane3,lane4,seconds):
    textlabel = ctk.CTkLabel(root,text="00:{}".format(seconds),font=("League Spartan",20))
    textlabel.place(x=100,y=100)
    def update_time():
        nonlocal seconds
        seconds -= 1
        if seconds <= 0:
           
            startLaneFour(root,lane1,lane2,lane3,lane4)
        else:
            textlabel.configure(text="00:{}".format(seconds))
            root.after(1000,update_time)
    
    update_time()





def startLaneOne(root,lane1,lane2,lane3,lane4):
    lane1.change_state(2)
    lane2.change_state(0)
    lane3.change_state(0)
    lane4.change_state(0)

def startLaneTwo(root,lane1,lane2,lane3,lane4):
    lane1.change_state(0)
    lane2.change_state(2)
    lane3.change_state(0)
    lane4.change_state(0)

def startLaneThree(root,lane1,lane2,lane3,lane4):
    lane1.change_state(0)
    lane2.change_state(0)
    lane3.change_state(2)
    lane4.change_state(0)
 
def startLaneFour(root,lane1,lane2,lane3,lane4):
    lane1.change_state(0)
    lane2.change_state(0)
    lane3.change_state(0)
    lane4.change_state(2)



def start():
   newWindow = ctk.CTkToplevel()
   newWindow.title("TraffAI")
   newWindow.geometry("900x900")
   cars = counter(video_array)

   cars.sort(reverse=True)
   lane1 = TrafficLight(newWindow,200,100)
   count1 = ctk.CTkLabel(master=newWindow,text="Vehicles : {}".format(cars[0]),font=("League Spartan",20))
   count1.place(x=280,y=110)


   lane2 = TrafficLight(newWindow,600,100)
   count2 = ctk.CTkLabel(master=newWindow,text="Vehicles : {}".format(cars[1]),font=("League Spartan",20))
   count2.place(x=680,y=110)
   

   lane3 = TrafficLight(newWindow,200,300)
   count3 = ctk.CTkLabel(master=newWindow,text="Vehicles : {}".format(cars[2]),font=("League Spartan",20))
   count3.place(x=280,y=310)


   lane4 = TrafficLight(newWindow,600,300)
   count4 = ctk.CTkLabel(master=newWindow,text="Vehicles : {}".format(cars[3]),font=("League Spartan",20))
   count4.place(x=680,y=310)
   secondsOne = int((cars[0]/ 2) + 5)
   countdownOne(newWindow,lane1,lane2,lane3,lane4,secondsOne,cars)


video1_button = ctk.CTkButton(master=app, text="Select Video 1", command=select_video1)
video1_button.place(relx=0.35, rely=0.5, anchor=ctk.CENTER)

video2_button = ctk.CTkButton(master=app, text="Select Video 2", command=select_video2)
video2_button.place(relx=0.65,rely=0.5, anchor=ctk.CENTER)

video3_button = ctk.CTkButton(master=app, text="Select Video 3", command=select_video3)
video3_button.place(relx=0.35,rely=0.7, anchor=ctk.CENTER)

video3_button = ctk.CTkButton(master=app, text="Select Video 4", command=select_video2)
video3_button.place(relx=0.65,rely=0.7, anchor=ctk.CENTER)

start_button = ctk.CTkButton(master=app,text="Start", command=start)
start_button.place(relx=0.5,rely=0.9,anchor=ctk.CENTER)

label = ctk.CTkLabel(master=app,text="TraffAI",font=("League Spartan",60))
label.place(relx=0.5,rely=0.1, anchor=ctk.CENTER)

label = ctk.CTkLabel(master=app, text="Empowering traffic management with intelligent insights", font=("League Spartan",20))
label.place(relx=0.5,rely=0.17, anchor=ctk.CENTER)

app.mainloop()