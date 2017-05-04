Chaos theory is a branch of physics and mathematics that focuses on the behavior of dynamical systems that are highly sensitive to initial conditions. An infinitesimally small change in initial condition would lead to a large change in state in a small amount of time; the errors in state grow exponentially over time. The systems are deterministic, which means that they are—rather than random—fully governed by a system of equations.

This project explores chaos as it analyzes, animates, and simulates a triple pendulum.

Code_Main.py calculates the numerical solution of a triple pendulum and writes the data to a user-named textfile. Based on constants and energies, the code calculates the equations of motion using the Lagrangian Method and computes the numerical solution using RK4. It uses the SymPy library to calculate derivatives. 

Animation_Main.py reads a user-defined textfile (ie Data_Main) and animates the results using Matplotlib. The textfile typically contains angular data, so it is necessary to convert the angles into coordinates. It may be necessary to manually update the length of any linkages.

The Documentation folder contains the final report, final presentation, and appropriate back-up files.

The Other folder contains alternative applications of the code, namely other applications of Lagrangian systems. These include a double pendulum, triple pendulum, and a pendulum spring.