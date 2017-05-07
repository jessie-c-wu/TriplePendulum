from __future__ import division,print_function
from numpy import array,arange,cos,sin,pi,savetxt,loadtxt
from pylab import plot,show
from matplotlib import pyplot as plt
from matplotlib import animation

fname1 = raw_input("1What file to read from? ")
data1 = loadtxt(fname1)
[theta1_pts, theta2_pts, theta3_pts,tpoints,E_pts] = data1

fname2 = raw_input("2What file to read from? ")
data2 = loadtxt(fname2)
[theta1_pts2, theta2_pts2, theta3_pts2,tpoints2,E_pts2] = data2

l1 = 0.4 # in
l2 = 0.4 # in
l3 = 0.4 # in

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

x02 = -l1/2*cos(theta1_pts2)
y02 = -l1/2*sin(theta1_pts2)
x12 = l1/2*cos(theta1_pts2)
y12 = l1/2*sin(theta1_pts2)
x22 = -l1/2*cos(theta1_pts2) + l2*cos(theta2_pts2)
y22 = -l1/2*sin(theta1_pts2) + l2*sin(theta2_pts2)
x32 = l1/2*cos(theta1_pts2) + l3*cos(theta3_pts2)
y32 = l1/2*sin(theta1_pts2) + l3*sin(theta3_pts2)


# Animation
fig = plt.figure()
ax = plt.axes(xlim=(-1, 1), ylim=(-1, 1))
line0, = ax.plot([], [], lw=2,marker='o',color='b')
line1, = ax.plot([], [], lw=2,marker='o',color='b')
line2, = ax.plot([], [], lw=2,marker='o',color='b')
line3, = ax.plot([], [], lw=2,marker='o',color='b')

line02, = ax.plot([], [], lw=2,marker='o',color='g')
line12, = ax.plot([], [], lw=2,marker='o',color='g')
line22, = ax.plot([], [], lw=2,marker='o',color='g')
line32, = ax.plot([], [], lw=2,marker='o',color='g')

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
	
    line12.set_data([], [])
    line22.set_data([], [])
    line32.set_data([], [])
    return line0,line1,line2,line3,line02,line12,line22,line32

def animate(i):
    i *= 2
    line0_x = array([0,x1[i]])
    line0_y = array([0,y1[i]])
    line1_x = array([x0[i],0])
    line1_y = array([y0[i],0])
    line2_x = array([x0[i],x2[i]])
    line2_y = array([y0[i],y2[i]])
    line3_x = array([x1[i],x3[i]])
    line3_y = array([y1[i],y3[i]])
    line0.set_data(line0_x, line0_y)
    line1.set_data(line1_x, line1_y)
    line2.set_data(line2_x, line2_y)
    line3.set_data(line3_x, line3_y)
	
    line0_x2 = array([0,x12[i]])
    line0_y2 = array([0,y12[i]])
    line1_x2 = array([x02[i],0])
    line1_y2 = array([y02[i],0])
    line2_x2 = array([x02[i],x22[i]])
    line2_y2 = array([y02[i],y22[i]])
    line3_x2 = array([x12[i],x32[i]])
    line3_y2 = array([y12[i],y32[i]])
    line02.set_data(line0_x2, line0_y2)
    line12.set_data(line1_x2, line1_y2)
    line22.set_data(line2_x2, line2_y2)
    line32.set_data(line3_x2, line3_y2)
    
    return line0,line1,line2,line3,line02,line12,line22,line32

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=25000000, interval = 0.040, blit=True)

## Plots
#plot(tpoints,E_pts)
#show()