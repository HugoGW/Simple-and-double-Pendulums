# Simple-and-double-Pendulums
Here are 2 Python codes: one to simulate the dynamics of N simple pendulums without friction, and another to simulate N double pendulums without friction.

I will detail the equations and the code that allowed me to obtain this result only for the double pendulum (it will be exactly the same for a simple pendulum).

First, take a pen and paper, and let's determine the equations of motion for the generalized coordinates $\theta_1$ and $\theta_2$ using the Euler-Lagrange equations: $\displaystyle \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{q}_i} - \frac{\partial \mathcal{L}}{\partial q_i} = 0$

It gives us 2 coupled diffenretial equations for $\theta_1$ and $\theta_2$.

$$
    \begin{array}{ll}
        \ddot{\theta}_1 = f_1(\theta_1, \dot{\theta}_1, \theta_2, \dot{\theta}_2) \\
        \ddot{\theta}_2 = f_2(\theta_1, \dot{\theta}_1, \theta_2, \dot{\theta}_2)
    \end{array}
$$
