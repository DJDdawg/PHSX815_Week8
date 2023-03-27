# PHSX815_Week8

**Neyman Plot**

HW8 had us convert the **Neyman.C** file from Professor Rogan (written in C++) into a Python file that creates the same Neyman Plot.

A Coin Flip is described by a Binomial Distribution, and only relies on one parameter p, the probability of Heads. 

In this simulation, a coin was flipped Nmeas times in each experiment, and this was repeated for Nexp experiments.

The Neyman plot has the x-axis as the "true value of p", and the y-axis as the "measured value of p in an experiment". 

The code file **Neyman_Plot.py** can be run with the following code:

> $ python3 Neyman_Plot.py -Nmeas 100 -Nexp 10000

This will flip a coin 100 times per experiment for 10,000 experiments. The large numbers for these two values gives small standard deviation in the measured values for p.

The output of this code can be seen in the figure **Neyman_Plot.png**.

The error bars on each data point represent a Gaussian distribution. A heatmap is also created for visual effect. Both plots show the same information.

![new](https://github.com/DJDdawg/PHSX815_Week8/blob/main/PHSX815_Week8/Neyman%20Plot.png)

The more measurements that are performed and the more experiments ran, the narrower the distribution becomes. The below graph uses 10 coin flips per experiment for 1000 experiments.

![new_1](https://user-images.githubusercontent.com/76142511/227788755-29ad4538-b134-41cf-af55-52c5bd800c76.png)


