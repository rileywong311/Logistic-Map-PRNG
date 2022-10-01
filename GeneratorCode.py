import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, chisquare
import time

# The generator


def intrin_gen(seed, iter_amount=20):  # iteration amounts per yield (changes statistical tests)
    r = 4                              # set steepness parameter
    a = 0.5                            # params for beta distribution
    b = 0.5
    x = seed * (1 - seed)              # using the seed as the initial condition and calculating the first step
    while True:                        # produce numbers indefinitely
        for _ in range(iter_amount):   # space out each yield
            x = r * x * (1 - x)        # logistic map equation
        yield beta.cdf(x, a, b)        # only apply beta CDF after doing regular iterations


# creating a class that uses a method to call next() on the generator object
class intrinsic_generator:
    def __init__(self, seed=None, iter_amount=None):
        # four possible setups for the intrinsic generator given optional seed and iter_amount
        if seed:
            if iter_amount:
                self.intrin_gen = intrin_gen(seed, iter_amount)
            else:
                self.intrin_gen = intrin_gen(seed)
        else:
            if iter_amount:
                self.intrin_gen = intrin_gen(seed_init(), iter_amount)
            else:
                self.intrin_gen = intrin_gen(seed_init())

    def gen(self):  # method that will call next() on the generator
        return next(self.intrin_gen)


# seed function
def seed_init():
    time_current = time.time()
    time_current = (time_current * 1000 % 1)  # returns number of centiseconds since last centisecond (from 0 to 1)
    return time_current


"""
# standard generation method
intrin = intrinsic_generator()

l = []
x_axis = range(10000)  # higher the range, smoother the histogram
for _ in x_axis:
    l.append(intrin.gen())  # creating a list


plt.figure(figsize=(30, 5))
plt.title("Sequence of Numbers Generated (first 500)")
plt.xlabel("Steps")
plt.ylabel("Value")
plt.plot(range(500), l[:500], ".-")
plt.figure()
plt.title("Distribution of Numbers Generated")
plt.xlabel("Value")
plt.ylabel("Amount")
plt.hist(l, bins=50)
plt.show()
"""