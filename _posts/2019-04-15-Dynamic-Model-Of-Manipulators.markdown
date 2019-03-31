---
layout: post
title: "Understanding Physics Engines: Dynamic Models of Manipulators"
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

$$ \dot q = \int \ddot q dt ,  \hspace{10mm} q = \int \dot q dt $$

**Inverse model:** once the joint accelerations, velocities and positions are known, compute the corresponding forces/torques

$$ \tau = f^{-1}(\ddot q, \dot q,  q) = g(\ddot q, \dot q, q) $$


From physics we know that it is possible to define: 

- The kinetic energy of the system, $$\mathcal{K}(q, \dot q)$$
- Potential energy of the system, $$\mathcal{P}(q)$$

Therefore, the Lagrangian is $$\mathcal{L}(q, \dot q) = \mathcal{K}(q, \dot q) - \mathcal{P}(q)$$.

The Euler-Lagrange equations are defined as 

$$\psi_i = \frac{d}{dt} \bigg( \frac{\partial \mathcal{L}}{\partial \dot q_i} \bigg) - \frac{\partial \mathcal{L}}{\partial \dot q_i} \hspace{10mm} i = 1, 2, \cdots, n $$

where $$\psi_i$$ is the non-conservative (external or dissipative) generalised forces performing any work on the joints $$q_i$$. It can be decomposed into:

- $$\tau_i$$, the joint actuator torque.
- $$J_i^T F_{c_i}$$, the term due to external forces.
- $$d_ii \dot q_i$$, joint friction torque.

Therefore, it can be written as $$\psi_i = \tau_i + J_i^T F_{c_i} - d_{ii}\dot q_i$$. Since the potential energy does not depend on the velocity, the euler-lagrange equation can be further simplied as 

$$\psi_i = \frac{d}{dt} \bigg( \frac{\partial \mathcal{K}}{\partial \dot q_i} \bigg) - \frac{\partial \mathcal{K}}{\partial \dot q_i} - \frac{\partial \mathcal{P}}{\partial \dot q_i}$$

Where $$\mathcal{K} = \sum_{i=1}^{n}\mathcal{K}_i \hspace{10mm} \mathcal{P} = \sum_{i=1}^{n}\mathcal{P}_i$$.

**Computing Kinetic Energy** 

- For any rigid body B, the _mass_ can be computed by integrating the mass density as: 

$$m = \int_{B} \rho(x, y, z)\hspace{1mm} dx dy dz$$ 

where the term $$\rho(x, y, z)$$ denotes the mass density and in some cases can be assumed constant, $$\rho$$.

- The _center of mass_ (CoM) can be computed as:

$$p_C = \frac{1}{m} \int_{B} p(x, y, z) \rho \hspace{1mm} dx dy dz$$ 

- The kinectic energy can be then written as:

$$\mathcal{K} = \frac{1}{2} \int_B v^T (x, y, z) v(x, y, z) \rho \hspace{1mm}dx dy dz$$

The velocity of a any point $p$ on a body undergoing motion in 3D can be written as 

$$v = v_C + \omega \times (p - p_C) = v_C + \omega \times r$$

The cross product with the angular velocity can be written as matrix vector product *i.e.* $$\omega \times r = S(\omega) r$$.

<center><img src="/assets/img/2019-04-15/linear_velocity.jpg" width="40%"></center>
credits: https://courses.lumenlearning.com/physics/chapter/10-1-angular-acceleration/

Therefore, the overall kinetic energy can be re-written as: 

$$
\begin{eqnarray*}
\mathcal{K}&=& \frac{1}{2} \int_B v^T (x, y, z) v(x, y, z) dm,\\
		    &=& \frac{1}{2} \int_B (v_C + Sr)^T (v_C + Sr) dm,\\
		    &=& \frac{1}{2} \int_B v_C^T v_C dm +  \frac{1}{2} \int_B r^T S^T Sr dm + \frac{1}{2} \int_B v_C^T Sr dm, \\
		    &=& \frac{1}{2} \int_B v_C^T v_C dm +  \frac{1}{2} \int_B r^T S^T Sr dm + 0
\end{eqnarray*}
$$

The expression $$ \frac{1}{2} \int_B v_C^T Sr \hspace{1mm} dm $$ sums to 0 *i.e.* 

$$ \int_B v_C^T Sr dm  = v_C^T S \int_B r dm = v_C^T S \int_B (p - p_C) dm = 0 $$

Further, using the identity $$a^Tb = Tr(a b^T)$$, we can rewrite the second term in the kinectic energy $$ \frac{1}{2} \int_B r^T S^T Sr dm $$  as:

$$
\begin{eqnarray*}
\frac{1}{2} \int_B r^T S^T Sr dm &=& \frac{1}{2} \int_B Tr(Sr r^T S^T) dm = \frac{1}{2} Tr \bigg( S \int_B rr^T dm  S^T\bigg), \\
							&=& Tr(S E S^T) = \frac{1}{2} \omega^T I \omega
\end{eqnarray*}
$$

where the matrix $$I$$ is the _body inertia matrix_. The matrix $$E$$ is the _Euler matrix_ and is:

$$
  E=
  \left[ {\begin{array}{ccc}
   \int r_x^2 dm & \int r_x r_y dm & \int r_x r_z dm\\
   \int r_x r_y dm & \int r_y^2 dm & \int r_y r_z dm\\
   \int r_x r_z dm & \int r_y r_z dm & \int r_z^2 dm\\
  \end{array} } \right]
$$

The inertia matrix is:

$$
  I=
  \left[ {\begin{array}{ccc}
   \int (r_y^2 +r_z^2) dm & -\int r_x r_y dm & -\int r_x r_z dm\\
   -\int r_x r_y dm & \int (r_x^2 + r_z^2) dm & -\int r_y r_z dm\\
   -\int r_x r_z dm & -\int r_y r_z dm & \int (r_x^2 + r_y^2) dm\\
  \end{array} } \right]
$$

The kinetic energy can be compactly written as: 

$$\mathcal{K} = \frac{1}{2} m v_C^T v_C + \frac{1}{2}\omega^T I \omega $$

This is also known as [_Konig Theorem_](https://en.wikipedia.org/wiki/K%C3%B6nig%27s_theorem_(kinetics)).

Thus, the kinect energy of an n-dof manipulator is 

$$\mathcal{K} = \frac{1}{2}\sum_{i=1}^n m_i v_{C_i}^T v_{C_i} + \frac{1}{2} \sum_{i=1}^n \omega_i^T R_i I_i R_i^T \omega_i $$

where 

- $$m_i$$ is the mass of the i-th link.
- $$v_{C_i}$$ is the linear velocity of the center of mass and $$\omega_i$$ is the rotatinal velocity of the link.
- $$I_i$$ is the inertial matrix computed in a fixed reference frame $$\mathcal{F}_i$$ attached to the center of the mass.
- $$R_i$$ is the rotation matrix of the link with respect to the fixed base frame $$\mathcal{F}_0$$.

$$
\begin{eqnarray*}
\mathcal{K} &=& \frac{1}{2}\sum_{i=1}^n m_i v_{C_i}^T v_{C_i} + \frac{1}{2} \sum_{i=1}^n \omega_i^T R_i I_i R_i^T \omega_i, \\
&=& \frac{1}{2}\dot q^T \sum_{i=1}^n \bigg[ m_i {J^i_v(q)}^T J^i_v(q) + {J^i_{\omega}(q)}^T R_i I_i R_i^T {J^i_{\omega}(q)} \bigg] \dot q
&=& \frac{1}{2}\dot q^T M(q) \dot q
&=& \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n M_{ij}(q) \dot q_i \dot q_j 
\end{eqnarray*}
$$


---
**NOTE**

It works with almost all markdown flavours (the below blank line matters).

---


> **_NOTE:_**  The note content. $$p_C = 3$$

