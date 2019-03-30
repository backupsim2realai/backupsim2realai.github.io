---
layout: post
title: "Dynamics Models of Manipulators"
date: 2019-04-15 13:32:20 +0100
description: describing the equations of motions as used in simulators # Add post description (optional)
img:  # Add image post (optional)
---

Robot Dynamics 

Study of the relation between the applied forces/torques and the resulting motion of an industrial manipulator.

Similarly to kinematics, also for the dynamics it is possible to define two “models”:


**Direct model:** once the forces/torques applied to the joints, as well as the joint positions and velocities are known, compute the joint accelerations: 
					$$ \ddot q = f (q, \dot q, \tau) $$
and then

$$ \dot q = \int \ddot q dt ,  \hspace{10mm} q = \int \ddot q dt $$

**Inverse model:** once the joint accelerations, velocities and positions are known, compute the corresponding forces/torques

$$ \tau = f^{-1}(\ddot q, \dot q,  q) = g(\ddot q, \dot q, q) $$


From physics we know that it is possible to define: 

- The kinetic energy of the system, $$\mathcal{K}(q, \dot q)$$
- Potential energy of the system, $$\mathcal{P}(q)$$

Therefore, the Lagrangian is $$\mathcal{L}(q, \dot q) = \mathcal{K}(q, \dot q) - \mathcal{P}(q)$$.

The Euler-Lagrange equations are defined as 

$$\psi_i = \frac{d}{dt} \bigg( \frac{\partial \mathcal{L}}{\partial \dot q_i} \bigg) - \frac{\partial \mathcal{L}}{\partial \dot q} \hspace{10mm} i = 1, 2, \cdots, n $$

where $$\psi_i$$ is the non-conservative (external or dissipative) generalised forces performing any work on the joints $$q_i$$. It can be decomposed into:

- $$\tau_i$$, the joint actuator torque.
- $$J_i^T F_c_i$$, the term due to external forces.
- $$d_ii \dot q_i$$, joint friction torque.

Therefore, it can be written as $$\psi_i = \tau_i + J_i^T F_c_i - d_ii\dot q_i$$.