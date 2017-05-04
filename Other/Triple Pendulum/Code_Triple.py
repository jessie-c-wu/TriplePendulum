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
ud1, ud2, ud3 = dynamicsymbols('u1 u2 u3', 1)

# Set Constants and Coefficients
m = 1.0   # kg 
g = 9.8   # m/s
l = 0.40  # m
I = 0.4   # Moment of Intertia CHANGE FOR I1
I1 = I / 4

M1 = 2.5*m*g*l
M2 = 1.5*m*g*l
M3 = 0.5*m*g*l
B1 = I + (l/2)**2*m + l**2*2*m
B2 = I + (l/2)**2*m + l**2*m
B3 = I + (l/2)**2*m
N12 = 1.5*m*l**2
N13 = 0.5*m*l**2
N23 = 0.5*m*l**2

V = -M1*cos(u1) - M2*cos(u2) - M3*cos(u3)
T = 0.5*(B1*ud1**2 + B2*ud2**2 + B3*ud3**2)
T += N12*ud1*ud2*cos(u1-u2) + N13*ud1*ud3*cos(u1-u3) + N23*ud2*ud3*cos(u2-u3)

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
b = 1e1     # Final time
h = 0.01 # Size of Runge-Kutta steps
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

    V = -M1*cos(r[0]) - M2*cos(r[1]) - M3*cos(r[2])
    T = 0.5*(B1*r[3]**2 + B2*r[4]**2 + B3*r[5]**2)
    T += N12*r[3]*r[4]*cos(r[0]-r[1]) + N13*r[3]*r[5]*cos(r[0]-r[2]) + N23*r[4]*r[5]*cos(r[1]-r[2])

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