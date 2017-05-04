from __future__ import division,print_function
from numpy import array,arange,cos,sin,pi,savetxt,loadtxt
from pylab import plot,show
from matplotlib import pyplot as plt
from matplotlib import animation

fname = raw_input("What file to read from? ")
data = loadtxt(fname)
[theta1_pts, theta2_pts, tpoints, E_pts] = data

l1 = 0.4 # in
l2 = 0.4 # in
l3 = 0.4 # in

# Calculate position from theta
# Pendulum 1 has endpoints (0,0) and (x1,y1)
x1 = (l1+theta1_pts)*sin(theta2_pts)
y1 = -(l1+theta1_pts)*cos(theta2_pts)

# Animation
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-100, 100))
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1,line2

def animate(i):
    i *= 1
    
    line1_x = array([0,x1[i]])
    line1_y = array([0,y1[i]])
    line2_x = array([0,0])
    line2_y = array([0,0])
    
    line1.set_data(line1_x, line1_y)
    line2.set_data(line2_x, line2_y)
    
    return line1,line2

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=250000, interval = 0.040, blit=True)

## Plots
#plot(tpoints,E_pts)
#show()