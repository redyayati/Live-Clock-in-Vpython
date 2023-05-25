from vpython import *
import numpy as np
import time
clock_radius=3
clock_thick=.1*clock_radius
tick_thick=.01*clock_radius
tick_small_length=.1*clock_radius
tick_big_length=.15*clock_radius
tick_radius=clock_radius-tick_big_length
second_theta=2*np.pi/60
seconds=0
count = 1
for my_angle in np.linspace(0,2*np.pi,60,False):
    small_ticks=cylinder(pos=vector((clock_radius-tick_small_length)*np.sin(my_angle),(clock_radius-tick_small_length)*np.cos(my_angle),clock_thick),
                axis=vector(np.sin(my_angle),np.cos(my_angle),0),radius=tick_thick,length=tick_small_length,color=color.black)
for my_angle in np.linspace(0,2*np.pi,12,False):
    big_ticks=cylinder(pos=vector((clock_radius-tick_big_length)*np.sin(my_angle),(clock_radius-tick_big_length)*np.cos(my_angle),clock_thick),
                axis=vector(np.sin(my_angle),np.cos(my_angle),0),radius=tick_thick+.02,length=tick_big_length,color=color.black)
clock_centerpin = cylinder(radius = clock_radius/15,
                            axis = vector(0,0,1), 
                            length = clock_thick+(2*tick_thick),
                            pos = vector(0,0,0),
                            color = color.black
                            )
clock_face=cylinder(pos=vector(0,0,0),axis=vector(0,0,1),radius=clock_radius,length=clock_thick,color=color.white)
my_label = text(text = 'India Time',pos=vector(0,1.1*clock_radius,0), align = 'center', color = color.orange,height=clock_radius/4, depth = clock_thick)

for my_angle in np.linspace((2*np.pi/12),(2*np.pi+(2*np.pi/12)),12,False):
    hour_text=text(text=str(count),
                   pos=vector((clock_radius*.75)*np.sin(my_angle),(clock_radius*.75)*np.cos(my_angle)-tick_small_length/2,clock_thick),
                   height=tick_small_length,color=color.orange,align='center',depth=clock_thick/2)
    count=count+1

sec_hand=arrow(axis=vector(0,1,0),pos=vector(0,0,clock_thick),length=(clock_radius-tick_small_length),color=color.blue,shaftwidth=tick_thick)
min_hand=arrow(axis=vector(0,1,0),pos=vector(0,0,clock_thick),length=(clock_radius-tick_small_length),color=color.red,shaftwidth=1.7*tick_thick)
hour_hand=arrow(axis=vector(0,1,0),pos=vector(0,0,clock_thick),length=(clock_radius-tick_small_length),color=color.green,shaftwidth=2.5*tick_thick)


while True:
    rate(100)
    my_time = time.localtime(time.time())
    hour = my_time[3] % 12
    minute = my_time[4]
    secs = my_time[5]
    theta_second_hand = secs*second_theta
    theta_minute_hand = theta_second_hand/60 + minute*2*np.pi/60
    theta_hour_hand = theta_minute_hand/12 + hour*2*np.pi/12
    sec_hand.axis=vector(np.sin(theta_second_hand),np.cos(theta_second_hand),0)
    sec_hand.length=(clock_radius-tick_small_length)
    min_hand.axis=vector(np.sin(theta_minute_hand),np.cos(theta_minute_hand),0)
    min_hand.length=(clock_radius-2*tick_small_length)
    hour_hand.axis=vector(np.sin(theta_hour_hand),np.cos(theta_hour_hand),0)
    hour_hand.length=(clock_radius-3*tick_small_length)
    
    
    
