# Simple-and-double-Pendulums
Here are 2 Python codes: one to simulate the dynamics of N simple pendulums without friction, and another to simulate N double pendulums without friction.

I will detail the equations and the code that allowed me to obtain this result only for the double pendulum (it will be exactly the same for a simple pendulum).

First, take a pen and paper, and let's determine the equations of motion for the generalized coordinates $\theta_1$ and $\theta_2$ using the Euler-Lagrange equations: $\displaystyle \frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot{q}_i} - \frac{\partial \mathcal{L}}{\partial q_i} = 0$

It gives us 2 coupled diffenretial equations for $\theta_1$ and $\theta_2$ :

$$
    \begin{array}{ll}
        \ddot{\theta}_1 = f_1(\theta_1, \dot{\theta}_1, \theta_2, \dot{\theta}_2) \\
        \ddot{\theta}_2 = f_2(\theta_1, \dot{\theta}_1, \theta_2, \dot{\theta}_2)
    \end{array}
$$

and we solve these ODEs with odeint from the scipy library. We repeat these process for N double pendulums and put all values in a matrix $\displaystyle [[\theta_1^1, \theta_2^1], [\theta_1^2, \theta_2^2], ..., [\theta_1^N, \theta_2^N]]$

Then, we choose our initial condition for our angles $\theta_1(t=0), \theta_2(t=0), \omega_1(t=0), \omega_2(t=0)$. In this code, I choose that my N double pendulums all have the same initial conditions except for $\displaystyle \theta_1^n(t=0) = \theta_1(t=0)\times n d\theta_1 \forall n \in \llbracket n~;~ p \rrbracket$

