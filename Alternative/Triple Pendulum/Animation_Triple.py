from __future__ import division,print_function
from numpy import array,arange,cos,sin,pi,savetxt,loadtxt
from pylab import plot,show
from matplotlib import pyplot as plt
from matplotlib import animation

fname = raw_input("What file to read from? ")
data = loadtxt(fname)
[theta1_pts, theta2_pts, theta3_pts,tpoints,E_pts] = data

l1 = 0.3 # in
l2 = 0.3 # in
l3 = 0.3 # in

# Calculate position from theta
# Pendulum 1 has endpoints (0,0) and (x0,y0)
# Pendulum 2 has endpoints (x0,y0) and (x1,y1)
# Pendulum 3 has endpoints (x1,y1) and (x2,y2)
x0 = l1*sin(theta1_pts)
y0 = -l1*cos(theta1_pts)
x1 = l1*sin(theta1_pts) + l1*sin(theta2_pts)
y1 = -l1*cos(theta1_pts) - l1*cos(theta2_pts)
x2 = l1*sin(theta1_pts) + l1*sin(theta2_pts) + l1*sin(theta3_pts)
y2 = -l1*cos(theta1_pts) - l1*cos(theta2_pts) - l1*cos(theta3_pts)

# Animation
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
line1, = ax.plot([], [], lw=2,marker='o',color='b')
line2, = ax.plot([], [], lw=2,marker='o',color='b')
line3, = ax.plot([], [], lw=2,marker='o',color='b')

line4, = ax.plot([], [], lw=1,color='k')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])    
    line4.set_data([], [])
    return line0,line1,line2,line3,line4

def animate(i):
    i *= 1
    line1_x = array([0,x0[i]])
    line1_y = array([0,y0[i]])
    line2_x = array([x0[i],x1[i]])
    line2_y = array([y0[i],y1[i]])
    line3_x = array([x1[i],x2[i]])
    line3_y = array([y1[i],y2[i]])
    line1.set_data(line1_x, line1_y)
    line2.set_data(line2_x, line2_y)
    line3.set_data(line3_x, line3_y)

    t = 40
    if i < t:
        j = 0
    else:
        j = i-t
    line4_x = array(x2[j:i])
    line4_y = array(y2[j:i])
   
    line4.set_data(line4_x, line4_y)

    return line1,line2,line3,line4

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=25000000, interval = 0.040, blit=True)

## Plots
#plot(tpoints,E_pts)
#show()