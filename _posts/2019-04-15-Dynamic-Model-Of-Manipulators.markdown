---
layout: post
title: "Understanding Physics Engines: Dynamic Models of Manipulators"
date: 2019-04-15 13:32:20 +0100
description: describing the equations of motions as used in simulators # Add post description (optional)
img:  # Add image post (optional)
---

Physics engines simulate a carefully approximated and idealised version of the real world. In recent times, the popularity of physics simulators has only increased among machine learning and computer vision practicioners. Being able to forward simulate the evolution of a physical world as a function of time --- under certain set of assumptions and approximations --- allows for optimising a control policy to carry out tasks. In this post, we will dive into the underlying maths and derive the fundamental equation that all physics engines implement to simulate dynamic model of an articulated manipulator.

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

Let us denote the $$i^{th}$$ joint by $$q_i$$ with $$\psi_i$$ being the non-conservative (external or dissipative) generalised forces performing any work on the joints $$q_i$$. It can be decomposed into:

- $$\tau_i$$, the joint actuator torque.
- $$J_i^\top F_{c_i}$$, the term due to external forces.
- $$d_{ii} \dot q_i$$, joint friction torque.

Therefore, it can be written as $$\psi_i = \tau_i + J_i^\top F_{c_i} - d_{ii}\dot q_i$$. Since the potential energy does not depend on the velocity, the euler-lagrange equation can be further simplied as 

$$\psi_i = \frac{d}{dt} \bigg( \frac{\partial \mathcal{K}}{\partial \dot q_i} \bigg) - \frac{\partial \mathcal{K}}{\partial \dot q_i} - \frac{\partial \mathcal{P}}{\partial \dot q_i}$$

Where $$\mathcal{K} = \sum_{i=1}^{n}\mathcal{K}_i \hspace{10mm} \mathcal{P} = \sum_{i=1}^{n}\mathcal{P}_i$$.

**Computing Kinetic Energy** 

For any rigid body B, the _mass_ can be computed by integrating the mass density as: 

$$m = \int_{B} \rho(x, y, z)\hspace{1mm} dx dy dz$$ 

where the term $$\rho(x, y, z)$$ denotes the mass density and in some cases can be assumed constant, $$\rho$$. The _center of mass_ (CoM) can be computed as:

$$p_C = \frac{1}{m} \int_{B} p(x, y, z) \rho \hspace{1mm} dx dy dz$$ 

The overall kinectic energy can be then written as:

$$\mathcal{K} = \frac{1}{2} \int_B v^\top (x, y, z) v(x, y, z) \rho \hspace{1mm}dx dy dz$$

We know that the velocity of a any point $p$ on a body undergoing motion in 3D can be written as 

$$v = v_C + \omega \times (p - p_C) = v_C + \omega \times r$$

Denoting $$r$$ by $$p - p_C$$ and writing the cross product as matrix vector product *i.e.* $$\omega \times r = S(\omega) r$$, the overall kinetic energy can be re-written as: 

$$
\begin{eqnarray*}
\mathcal{K}&=& \frac{1}{2} \int_B v^\top (x, y, z) v(x, y, z) dm,\\
		    &=& \frac{1}{2} \int_B (v_C + \mathsf{S}r)^\top (v_C + \mathsf{S}r) dm,\\
		    &=& \frac{1}{2} \int_B v_C^\top v_C dm +  \frac{1}{2} \int_B r^\top S^\top Sr dm + \frac{1}{2} \int_B v_C^\top \mathsf{S}r dm, \\
		    &=& \frac{1}{2} \int_B v_C^\top v_C dm +  \frac{1}{2} \int_B r^\top S^\top \mathsf{S}r dm + 0
\end{eqnarray*}
$$

The expression $$ \frac{1}{2} \int_B v_C^\top Sr \hspace{1mm} dm $$ sums to 0 *i.e.* 

$$ \int_B v_C^\top Sr dm  = v_C^\top S \int_B r dm = v_C^\top S \int_B (p - p_C) dm = 0 $$

Further, using the identity $$a^\top b = Tr(a b^\top)$$, we can rewrite the second term in the kinectic energy $$ \frac{1}{2} \int_B r^\top S^\top Sr dm $$  as:

$$
\begin{eqnarray*}
\frac{1}{2} \int_B r^\top S^\top Sr dm &=& \frac{1}{2} \int_B Tr(Sr r^\top S^\top) dm = \frac{1}{2} Tr \bigg( S \int_B rr^\top dm  S^\top\bigg), \\
							&=& Tr(S E S^\top) = \frac{1}{2} \omega^\top I \omega
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

$$\mathcal{K} = \frac{1}{2} m v_C^\top v_C + \frac{1}{2}\omega^\top I \omega $$

This is also known as [_Konig Theorem_](https://en.wikipedia.org/wiki/K%C3%B6nig%27s_theorem_(kinetics)).

Thus, the kinect energy of an n-dof manipulator is 

$$\mathcal{K} = \frac{1}{2}\sum_{i=1}^n m_i v_{C_i}^\top v_{C_i} + \frac{1}{2} \sum_{i=1}^n \omega_i^\top R_i I_i R_i^\top \omega_i $$

where 

- $$m_i$$ is the mass of the i-th link.
- $$v_{C_i}$$ is the linear velocity of the center of mass and $$\omega_i$$ is the rotatinal velocity of the link.
- $$I_i$$ is the inertial matrix computed in a fixed reference frame $$\mathcal{F}_i$$ attached to the center of the mass.
- $$R_i$$ is the rotation matrix of the link with respect to the fixed base frame $$\mathcal{F}_0$$.

Representing the end-effector position with respect to the base frame we have the following expression 

$$r_{be} = \texttt{f}(q)$$

We can differentiate this and get the velocity of end-effector position as a function of angles $$q$$

$$\dot{r}_{be} \approx  \frac{\partial \texttt{f}(q)}{\partial q} \dot{q} = \texttt{J} \dot{q}$$

Denoting the velocity $$\dot{r}_{be}$$ as $$v_{be}$$, we can express it recursively for any link $$k$$ as 

$$ v_{bk} = v_{b(k-1)} + \omega_{b(k-1)} \times r_{(k-1)k} $$

Assuming the end-effector frame is denoted by $$n+1$$, the velocity of the end-effector can be re-written as 

$$ v_{bk} = \sum_{k=1}^{n} \omega_{bk} \times r_{k(k+1)} $$

Let us denote $$z_k$$ to be the axis of rotation of joint $$k$$. We can rewrite the angular velocity of joint $$k$$ wrt to $$k-1$$ as 

$$ \omega_{(k-1)k} = z_k \dot{q}_k$$ 

Also, we know that

$$\omega_{bk} = \omega_{b(k-1)} + \omega_{(k-1)k}$$

Therefore, the angular velocity of link $$k$$ can be written as 

$$\omega_{bk} = \sum_{i=1}^{k} z_i \dot{q}_i$$

Plugging this expression back into the link velocity equation we get 

$$v_{be} = \sum_{k=1}^{n} \sum_{i=1}^{k} z_i \dot{q}_i \times r_{k(k+1)}$$

$$v_{be} = \sum_{k=1}^{n} z_k \dot{q}_k \times \sum_{i=k}^{n} r_{i(i+1)}$$

$$v_{be} = \sum_{k=1}^{n} z_k \dot{q}_k \times r_{k(n+1)}$$

$$\mathbf{v}_{be}=\underbrace{\left[\mathbf{z}_{1} \times \mathbf{r}_{1(n+1)} \quad \mathbf{z}_{2} \times \mathbf{r}_{2(n+1)} \quad \ldots \quad \mathbf{z}_{n} \times \mathbf{r}_{n(n+1)}\right]}_{\mathbf{J}_{\mathrm{be}}}\left(\begin{array}{c}{\dot{q}_{1}} \\ {\dot{q}_{2}} \\ {\vdots} \\ {\dot{q}_{n}}\end{array}\right)$$

$$
\begin{eqnarray*}
\mathcal{K} &=& \frac{1}{2}\sum_{i=1}^n m_i v_{C_i}^\top v_{C_i} + \frac{1}{2} \sum_{i=1}^n \omega_i^\top R_i I_i R_i^\top \omega_i, \\
&=& \frac{1}{2}\dot q^\top \sum_{i=1}^n \bigg[ m_i {J^i_v(q)}^\top J^i_v(q) + {J^i_{\omega}(q)}^\top R_i I_i R_i^\top {J^i_{\omega}(q)} \bigg] \dot q
&=& \frac{1}{2}\dot q^\top M(q) \dot q
&=& \frac{1}{2} \sum_{i=1}^n \sum_{j=1}^n M_{ij}(q) \dot q_i \dot q_j 
\end{eqnarray*}
$$


Blog: https://conversationofmomentum.wordpress.com/2014/08/05/euler-lagrange-equations/

ETH Dynamics: https://www.ethz.ch/content/dam/ethz/special-interest/mavt/robotics-n-intelligent-systems/rsl-dam/documents/RobotDynamics2016/6-dynamics.pdf

How physics engines work https://www.haroldserrano.com/blog/how-a-physics-engine-works-an-overview

Sweep and Prune: https://github.com/mattleibow/jitterphysics/wiki/Sweep-and-Prune
---
**NOTE**

It works with almost all markdown flavours (the below blank line matters).

---


> **_NOTE:_**  The note content. $$p_C = 3$$

