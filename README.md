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

Then, we choose our initial condition for our angles $\theta_1(t=0), \theta_2(t=0), \omega_1(t=0), \omega_2(t=0)$. In this code, I choose that my N double pendulums all have the same initial conditions except for $\displaystyle \theta_1^k(t=0) = \theta_1(t=0)\times k d\theta_1 ~~ \forall ~ k \in  {1,...,N}$.

Once every couple of angle [\theta_1^k, \theta_2^k] solved, we determine the position of the masses of the double pendulum with polar coordinates (by taking into account that the zero angle starts at $-\pi /2$ on the unit circle because $\vec{g} // -\vec{e}_y$: 

$$
    \begin{array}{ll}
        x_1^k = L_1 \sin(\theta_1^k) \\
        y_1^i = -L_1 \cos(\theta_1^k) \\
        x_2^i = x_1^k + L_2 \sin(\theta_2^k) \\
        y_2^i = y_1^k -L_2 \cos(\theta_2^k) \\
    \end{array}
$$

Then, we animate our 2N angles in function of time by using FuncAnimation from the matplotlib.animation library.

https://github.com/HugoGW/Simple-and-double-Pendulums/assets/140922475/858d2216-4e0f-45c1-a99a-05b943aec61f

We could add dots to explicitly show the masses but I find it more elegant without them.

We could also plot the behavior of the 2 angles in their respective phase spaces, which could be interesting.
We could improve our model by considering friction.



