from __future__ import division,print_function
from numpy import array,arange,cos,sin,pi,savetxt,loadtxt
from pylab import plot,show
from matplotlib import pyplot as plt
from matplotlib import animation

fname = raw_input("What file to read from? ")
data = loadtxt(fname)
[theta1_pts, theta2_pts, tpoints,E_pts] = data

fname2 = raw_input("2What file to read from? ")
data2 = loadtxt(fname2)
[theta1_pts2, theta2_pts2, tpoints2,E_pts2] = data2

l1 = 0.4 # in
l2 = 0.4 # in
l3 = 0.4 # in

# Calculate position from theta
# Pendulum 1 has endpoints (0,0) and (x1,y1)
# Pendulum 2 has endpoints (x1,y1) and (x2,y2)
x1 = l1*sin(theta1_pts)
y1 = -l1*cos(theta1_pts)
x2 = l1*sin(theta1_pts) + l2*sin(theta2_pts)
y2 = -l1*cos(theta1_pts) - l2*cos(theta2_pts)

x12 = l1*sin(theta1_pts2)
y12 = -l1*cos(theta1_pts2)
x22 = l1*sin(theta1_pts2) + l2*sin(theta2_pts2)
y22 = -l1*cos(theta1_pts2) - l2*cos(theta2_pts2)


# Animation
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
line12, = ax.plot([], [], lw=2)
line22, = ax.plot([], [], lw=2)


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line12.set_data([], [])
    line22.set_data([], [])
    return line1,line2,line12,line22

def animate(i):
    i *= 1
    line1_x = array([0,x1[i]])
    line1_y = array([0,y1[i]])
    line2_x = array([x1[i],x2[i]])
    line2_y = array([y1[i],y2[i]])

    line1_x2 = array([0,x12[i]])
    line1_y2 = array([0,y12[i]])
    line2_x2 = array([x12[i],x22[i]])
    line2_y2 = array([y12[i],y22[i]])
    
    line1.set_data(line1_x, line1_y)
    line2.set_data(line2_x, line2_y)
    line12.set_data(line1_x2, line1_y2)
    line22.set_data(line2_x2, line2_y2)
    
    return line1,line2,line12,line22

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=250000, interval = 0.040, blit=True)

## Plots
#plot(tpoints,E_pts)
#show()