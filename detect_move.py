"""
Basic Robot Moving round arena using Python and TKinter
"""
import time
import random
# Get TKinter ready to go
from tkinter import *
window = Tk()
canvas = Canvas(window, width=400, height=300, bg='white')
canvas.pack(padx=10,pady=10)
# The velocity, or distance moved per time step
vx = 10.0 # x velocity
vy = 5.0 # y velocity
# Boundaries
x_min = 0.0
y_min = 0.0
x_max = 400.0
y_max = 300.0
id1=canvas.create_rectangle(3,7,3+10,7+10)
Obx1=random.randint(75,250)
Oby1=random.randint(75,250)
Obx2=Obx1+150
Oby2=Oby1-75
#count for steps to move away from the objects
count=0
#create object to avoid
id2=canvas.create_rectangle(Obx1,Oby1,Obx2,Oby2, fill='blue')
# Generate x and y coordinates for 500 timesteps
for t in range(1, 500):
    x1,y1,x2,y2=canvas.coords(id1)
    #Detect left side of object
    if x2>(Obx1 - 10) and x2<(Obx1+10) and y1< Oby1 and y1>Oby2:
        #Detect right side of object
        print ("Object detected left side")
    if x1<(Obx2 + 10) and x1>(Obx2 - 10)and y1< Oby1 and y1>Oby2:
        count=1
        print ("Object detected right side")
        #Detect Bottom of object
    if y1>(Oby1 - 10) and y1<(Oby1+10) and x1>Obx1 and x1<Obx2:
        print ("Object detected bottom of object")
    #Detect top of object
    if y1>(Oby2 - 10) and y1<(Oby2+10) and x1>Obx1 and x1<Obx2:
        count=1
        print ("Object detected top of object")
    #if counter set move away from left side or bottom of object
    if count>0:
        vx=+10
        vy=-5
        count=count-1
    # If a boundary has been crossed, reverse the direction
    if x1 >= x_max:
        vx = -10.0
    if y1 <= y_min:
        vy = 5.0
    if y2 >= y_max:
        vy = -5.0
    if x1 <= x_min:
        vx = 10.0
    # Reposition the robot
    canvas.coords(id1,x1+vx,y1+vy,x2+vx,y2+vy)
    canvas.update()
    # Pause for 0.1 seconds, then delete the image
    time.sleep(0.1)
window.mainloop()
