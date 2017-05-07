from __future__ import division,print_function
from numpy import array,arange,pi,zeros,savetxt,loadtxt
from pylab import plot,show
from sympy import cos,sin
from sympy.physics.mechanics import *
from time import time

# Jessie Wu, PH235 Final Project, Spring 2017
# The program writes the data for the motion of a triple pendulum given initial conditions
# Inputs are system dimensions and a Lagrange equation 
# Sympy library computes derivatives and outputs EOM as 6 simaltaneous 1st-order ODE
# Use RK4 to numerically solve and output

## TOGGLES: h step, r initial condition
## 

## INITIALIZE and find EQUATION OF MOTION

# Declare Dynamic Variables
u1, u2 = dynamicsymbols('u1 u2')
u1d, u2d = dynamicsymbols('u1 u2', 1)

# Set Constants and Coefficients
m = 1.0   # kg 
g = 9.8   # m/s
l = 0.40  # m
I = 0.4   # Moment of Intertia CHANGE FOR I1
I1 = I / 4

c1 = -2*m*g*l
c2 = -m*g*l
c3 = m*l**2
c4 = 0.5*m*l**2
c5 = m*l**2

# Calculate Kinetic, Potential, and Lagrangian
V = c1*cos(u1) + c2*cos(u2)
T = c3*u1d**2 + c4*u2d**2 + c5*u1d*u2d*cos(u1-u2) 

L = T - V

# Form EOM
LM = LagrangesMethod(L, [u1, u2])
mechanics_printing(pretty_print=False)
LM.form_lagranges_equations()
EOM = LM.rhs()
r_new = zeros(4)

print("Finished calculating EOM")
raw_input("Ready to run RK4 algorithm? : ")
print("Calculating...")

def f(r):
    # EOM is of the form [u1 u2 u1d u2d]
    # Substitute r values into EOM using subs and msubs
    subs = {u1:r[0],u2:r[1],u1.diff():r[2],u2.diff():r[3]}
    dummy = msubs(EOM,subs)
    # Convert from Matrix into Array, and output array
    for j in range(len(EOM)):
        r_new[j] = dummy[j]
    return r_new

## Time Step and Arrays
a = 0       # Initial time
b = 1e2    # Final time
h = 0.01 # Size of Runge-Kutta steps
tpoints = arange(a,b,h)

theta1_pts = []
theta2_pts = []
E_pts = []
i = 1
print("Total Points:")
print(len(tpoints))
start = time()

r = array([pi/2,0,0,0],float) # SET INITIAL CONDITIONS [u1 u2 ud1 ud2]

## Run through RK4 for time steps
for t in tpoints:
    theta1_pts.append(r[0])
    theta2_pts.append(r[1])
    
    # Energy calculation
	
    V = c1*cos(r[0]) + c2*cos(r[1])
    T = c3*r[2]**2 + c4*r[3]**2 + c5*r[2]*r[3]*cos(r[0]-r[1])
    E = T + V
    E_pts.append(E)
    
    # Algorithm for a 4th Order Runge-Kutta
    k1 = h*f(r)
    k2 = h*f(r+0.5*k1)
    k3 = h*f(r+0.5*k2)
    k4 = h*f(r+k3)
    r += (k1+2*k2+2*k3+k4)/6

    # Print Status and Time
    end = time() - start
    if i%200 == 0:
        print(i)
        print(end/60)
    i += 1

print("Done calculating, writing output")
fname = raw_input("What to name output file? : ")
savetxt(fname, (theta1_pts,theta2_pts,tpoints,E_pts))