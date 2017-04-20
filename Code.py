from __future__ import division,print_function
from numpy import array,arange,cos,sin,pi,savetxt,loadtxt
from pylab import plot,show
from matplotlib import pyplot as plt
from matplotlib import animation

## Physical Set-Up
# Constants
rho = 0.098*12**3 # lbm/in^3
t = 0.25/12 # in
g = 32.2 # in/s^2
l1 = 6/12 # in
l2 = 4/12 # in
l3 = 4/12 # in
m1 = rho*t*l1*1 # lbm
m2 = rho*t*l2*1 # lbm
m3 = rho*t*l3*1 # lbm
I1 = m1*l1**2/12
I2 = m2*l2**2/3
I3 = m3*l2**2/3

# Coefficients
c1 = m2*l1**2/2 + m3*l1**2/2 + I1/2
c2 = m2*l2**2/2 + I2/2
c3 = m3*l3**2/2 + I3/2
c5 = -l2*m2*g
c6 = -l3*m3*g
c7 = -l1*l2*m2
c8 = l1*l3*m3

def f(r):
	## Equations of Motion for a Triple Pendulum
	## Rewrite 3 Second Order Differential Equations as Six Simultaneous First Order Differential Equations
	## Refer to Appendix for Derivation
	
	# Define Angles
	theta_1 = r[0]
	theta_dot_1 = r[1]
	theta_2 = r[2]
	theta_dot_2 = r[3]
	theta_3 = r[4]
	theta_dot_3 = r[5]

	# Set Up
	A = c7*cos(theta_2-theta_1)/(2*c2)*(c5*cos(theta_2) - c7*theta_dot_1*theta_dot_2*sin(theta_2-theta_1) + c7*theta_dot_1*(theta_dot_2-theta_dot_1)*sin(theta_2-theta_1)) 
	B = c8*cos(theta_3-theta_1)/(2*c3)*(c6*cos(theta_3) - c8*theta_dot_1*theta_dot_3*sin(theta_3-theta_1) + c8*theta_dot_1*(theta_dot_3-theta_dot_1)*sin(theta_3-theta_1))
	C = c7*theta_dot_1*theta_dot_2*sin(theta_2-theta_1) + c8*theta_dot_1*theta_dot_3*sin(theta_3-theta_1) + c7*(theta_dot_2-theta_dot_1)*theta_dot_2*sin(theta_2-theta_1) + c8*(theta_dot_3-theta_dot_1)*theta_dot_3*sin(theta_3-theta_1)
	D = 2*c1 - c7**2*(cos(theta_2-theta_1))**2/(2*c2) - c8**2*(cos(theta_3-theta_1))**2/(2*c3)


	
	# Equations of Motion
	ftheta_1 = theta_dot_1
	theta_ddot_1 = (C - A - B)/D
	ftheta_2 = theta_dot_2
	theta_ddot_2 = -c7*cos(theta_2-theta_1)/(2*c2)*(C - B - A)/D + A/(2*c2)
	ftheta_3 = theta_dot_3
	theta_ddot_3 = -c8*cos(theta_3-theta_1)/(2*c3)*(C - B - A)/D + B/(2*c3)
	
	return array([ftheta_1,theta_ddot_1,ftheta_2,theta_ddot_2,ftheta_3,theta_ddot_3],float)

## Initialization
a = 0       # Initial time
b = 1e1     # Final time
N = 7e5    # Number of Runge-Kutta steps
h = (b-a)/N # Size of Runge-Kutta steps
tpoints = arange(a,b,h)

theta1_pts = []
theta2_pts = []
theta3_pts = []
E_pts = []

r = array([0,1,pi/2,0,pi/2,0],float) # SET INITIAL CONDITIONS [angle, speed]

#Print Calculating? Perhaps estimate on time step. Confirm h and initial conditions.

## Run through RK4 for time steps
for t in tpoints:
    theta1_pts.append(r[0])
    theta2_pts.append(r[2])
    theta3_pts.append(r[4])
    
    # Energy calculation
    T = c1*r[1]**2 + c2*r[3]**2 + c3*r[5]**2 + c7*cos(r[2]-r[0])*r[1]*r[3] + c8*cos(r[4]-r[0])*r[1]*r[5]
    V = -(c5*sin(r[2]) + c6*sin(r[4]))
    E = T + V
    E_pts.append(E)
    
    # Algorithm for a 4th Order Runge-Kutta
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    r += (k1+2*k2+2*k3+k4)/6

savetxt('test4.txt', (theta1_pts,theta2_pts,theta3_pts,tpoints,E_pts))
