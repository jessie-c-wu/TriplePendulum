from __future__ import division,print_function
from numpy import array,arange,cos,sin,pi,savetxt,loadtxt
from pylab import plot,show
from matplotlib import pyplot as plt
from matplotlib import animation

data = loadtxt("test4.txt")
[theta1_pts, theta2_pts, theta3_pts,tpoints,E_pts] = data

l1 = 6/12 # in
l2 = 4/12 # in
l3 = 4/12 # in

# Calculate position from theta
# Pendulum 1 has endpoints (x0,y0) and (x1,y1)
# Pendulum 2 has endpoints (x0,y0) and (x2,y2)
# Pendulum 3 has endpoints (x1,y1) and (x3,y3)
x0 = -l1/2*cos(theta1_pts)
y0 = -l1/2*sin(theta1_pts)
x1 = l1/2*cos(theta1_pts)
y1 = l1/2*sin(theta1_pts)
x2 = -l1/2*cos(theta1_pts) + l2*cos(theta2_pts)
y2 = -l1/2*sin(theta1_pts) + l2*sin(theta2_pts)
x3 = l1/2*cos(theta1_pts) + l3*cos(theta3_pts)
y3 = l1/2*sin(theta1_pts) + l3*sin(theta3_pts)

# Animation
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
line3, = ax.plot([], [], lw=2)

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    return line1,line2,line3

def animate(i):
    i *= 200
    line1_x = array([x0[i],x1[i]])
    line1_y = array([y0[i],y1[i]])
    line2_x = array([x0[i],x2[i]])
    line2_y = array([y0[i],y2[i]])
    line3_x = array([x1[i],x3[i]])
    line3_y = array([y1[i],y3[i]])
    line1.set_data(line1_x, line1_y)
    line2.set_data(line2_x, line2_y)
    line3.set_data(line3_x, line3_y)
    
    return line1,line2,line3

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=250000, interval = 0.040, blit=True)

# Plots
plot(tpoints,E_pts)
show()