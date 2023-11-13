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
     \sqrt{\langle x_n^2 \rangle} = \sqrt{(\sum_{i=1}^{n}\langle \Delta x_i )^2\rangle } = \sqrt{\sum_{i=1}^n \langle\Delta x_i^2\rangle + 2 \sum_{i<j}\langle \Delta x_i  \Delta x_j \rangle} = \sqrt{(\frac{1}{3}(-1)^2+\frac{1}{3}(0)^2 + \frac{1}{3}(1)^2) + 0} = \sqrt{\frac{2}{3}}.
$$

### Comments