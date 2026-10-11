# Gravitational N-Body Simulation

## Overview

An independent computational physics project exploring gravitational orbital dynamics through numerical integration in Python.

The project models gravitational interactions using Newton's law of universal gravitation and investigates how numerical methods approximate the motion of celestial bodies.

## Physics

The gravitational force between two bodies is calculated using:

\[
\vec F_{ij}=-\frac{Gm_im_j}{|\vec r_i-\vec r_j|^3}(\vec r_i-\vec r_j)
\]

The simulation uses astronomical units, solar masses, and years, with \(G=4\pi^2\).

## Numerical Methods

The current implementation uses Euler-Cromer integration to update velocity and position at discrete time steps.

The project explores numerical accuracy, accumulated integration error, and the stability of orbital trajectories.

Tools

- Python
- NumPy
- Matplotlib

Current Development

- Earth–Sun orbital integration
- Trajectory visualization
- Extension to a fully coupled Sun–Earth–Moon simulation
- Evaluation of numerical accuracy and conservation of energy

Motivation

This project was developed to strengthen my understanding of numerical methods, computational physics, and the relationship between mathematical models and physical systems.
