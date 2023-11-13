# H23_project3_kjesta
## Project 3 for kjesta (kjesta@mail.uio.no)

- Repo url : https://github.uio.no/IN1910/H23_project3_kjesta

## Authors

- Kjersti Stangeland (kjesta@geo.uio.no)

### Answers to task 1c)
Mean displacement at time step $n$ is given by
$$
    \langle x_n \rangle = \sum_{i=1}^{n} \langle \Delta x_i \rangle,
$$
$$

    \langle \Delta x_i \rangle = \sum_{\alpha} = p^{\alpha}\Delta x^{\alpha} = \frac{1}{3} (-1) + \frac{1}{3} (0) + \frac{1}{3} (1) = 0
$$
while the RMS is given by
$$
     \sqrt{\langle x_n^2 \rangle} = \sqrt{(\sum_{i=1}^{n}\langle \Delta x_i )^2\rangle } = \sqrt{\sum_{i=1}^n \langle\Delta x_i^2\rangle + 2 \sum_{i<j}\langle \Delta x_i  \Delta x_j \rangle} =
$$
$$ 
      \sqrt{\sum _{i=1}^{n}(\frac{1}{3}(-1)^2+\frac{1}{3}(0)^2 + \frac{1}{3}(1)^2) + 0} = \sqrt{\frac{2n}{3}}.
$$

### Answers to task 1d)
- The plot "statistical_1D.png" shows that the law of large numbers holds. The calculated values from the random walks gets closer to the analytical solution as numbers of walkers increases. With M = 1000, the calculated value does not deviate too much from the analytical value, and seems to develop in the same nature.

### Answers to task 2c)
Mean displacement at time step $n$ is given by
$$
\langle \vec r_n \rangle = (\langle x_n \rangle, \langle y_n \rangle) = (\sum_{i=1}^{n} \langle \Delta x_i \rangle, \sum_{i=1}^{n} \langle \Delta y_i \rangle) =
$$
$$ \sum_{i=1}^{n}( \frac{1}{3} (-1) + \frac{1}{3} (0) + \frac{1}{3} (1),  \frac{1}{3} (-1) + \frac{1}{3} (0) + \frac{1}{3} (1)) = (0,0)
$$

while the RMS is given by

$$
\sqrt{\langle \lvert \vec r_n \rvert^2 \rangle} = \sqrt{\langle x_n ^2 \rangle, \langle y_n ^2 \rangle} = \sqrt{(\sum_{i=1}^{n} \langle \Delta x_i ^2\rangle, \sum_{i=1}^{n} \langle \Delta y_i ^2 \rangle)} 
$$

$$
= \sqrt{(\sum_{i=1}^n(\frac{1}{3} (-1)^2 + \frac{1}{3} (0)^2 + \frac{1}{3} (1)^2),  \sum_{i=1}^n(\frac{1}{3} (-1)^2 + \frac{1}{3} (0)^2 + \frac{1}{3} (1)^2))}
$$

$$
= \sqrt{(\frac{2n}{3}, \frac{2n}{3})}
$$


### Comments