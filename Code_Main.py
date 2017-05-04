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
u1, u2, u3 = dynamicsymbols('u1 u2 u3')
u1d, u2d, u3d = dynamicsymbols('u1 u2 u3', 1)

# Set Constants and Coefficients
m = 1.0   # kg 
g = 9.8   # m/s
l = 0.40  # m
I = 0.4   # Moment of Intertia CHANGE FOR I1
I1 = I / 4

c1 = m*l**2/2 + m*l**2/2 + I1/2
c2 = m*l**2/2 + I/2
c3 = m*l**2/2 + I/2
c5 = l*m*g
c6 = l*m*g
c7 = -l**2*m
c8 =l**2*m

# Calculate Kinetic, Potential, and Lagrangian
T = c1*u1d**2 + c2*u2d**2 + c3*u3d**2 + c7*u1d*u2d*cos(u2-u1) + c8*u1d*u3d*cos(u3-u1)
V = c5*sin(u2) + c6*sin(u3)

L = T - V

# Form EOM
LM = LagrangesMethod(L, [u1, u2, u3])
mechanics_printing(pretty_print=False)
LM.form_lagranges_equations()
EOM = LM.rhs()
r_new = zeros(6)

print("Finished calculating EOM")
raw_input("Ready to run RK4 algorithm? : ")
print("Calculating...")

def f(r):
    # EOM is of the form [u1 u2 u3 u1d u2d u3s]
    # Substitute r values into EOM using subs and msubs
    subs = {u1:r[0],u2:r[1],u3:r[2],u1.diff():r[3],u2.diff():r[4],u3.diff():r[5]}
    dummy = msubs(EOM,subs)
    # Convert from Matrix into Array, and output array
    for i in range(len(EOM)):
        r_new[i] = dummy[i]
    return r_new

## Time Step and Arrays
a = 0       # Initial time
b = 0.31     # Final time
h = 0.0001 # Size of Runge-Kutta steps
tpoints = arange(a,b,h)

# TEST 0.1, 0.05, 0.025, 0.0125

theta1_pts = []
theta2_pts = []
theta3_pts = []
E_pts = []
i = 1
print("Total Points:")
print(len(tpoints))
start = time()

r = array([pi/2,-pi/2,pi/4,0,0,0],float) # SET INITIAL CONDITIONS [u1 u2 u3 ud1 ud2 ud3]

## Run through RK4 for time steps
for t in tpoints:
    theta1_pts.append(r[0])
    theta2_pts.append(r[1])
    theta3_pts.append(r[2])
    
    # Energy calculation
    T = c1*r[3]**2 + c2*r[4]**2 + c3*r[5]**2 + c7*r[3]*r[4]*cos(r[1]-r[0]) + c8*r[3]*r[5]*cos(r[2]-r[0])
    V = c5*sin(r[1]) + c6*sin(r[2])
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
savetxt(fname, (theta1_pts,theta2_pts,theta3_pts,tpoints,E_pts))