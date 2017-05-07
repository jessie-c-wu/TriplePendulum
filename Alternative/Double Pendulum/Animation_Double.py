from __future__ import division,print_function
from numpy import array,arange,cos,sin,pi,savetxt,loadtxt
from pylab import plot,show
from matplotlib import pyplot as plt
from matplotlib import animation

fname = raw_input("What file to read from? ")
data = loadtxt(fname)
[theta1_pts, theta2_pts, tpoints,E_pts] = data

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

# Animation
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
line1, = ax.plot([], [], lw=2,marker='o',color='b')
line2, = ax.plot([], [], lw=2,marker='o',color='b')
line3, = ax.plot([], [], lw=1,color="k")


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1,line2,line3

def animate(i):
    i *= 1
    line1_x = array([0,x1[i]])
    line1_y = array([0,y1[i]])
    line2_x = array([x1[i],x2[i]])
    line2_y = array([y1[i],y2[i]])

    line1.set_data(line1_x, line1_y)
    line2.set_data(line2_x, line2_y)
    
    t = 20
    if i < t:
        j = 0
    else:
        j = i-t
    line3_x = array(x2[j:i])
    line3_y = array(y2[j:i])
   
    line3.set_data(line3_x, line3_y)

    return line1,line2,line3
    
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=250000, interval = 0.040, blit=True)

## Plots
#plot(tpoints,E_pts)
#show()