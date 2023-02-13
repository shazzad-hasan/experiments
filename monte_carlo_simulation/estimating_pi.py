
import random
import math
random.seed(100)


def in_circle(x, y, r):
    """
    Return True if the point is in the circle,
           False otherwise.
    """
    return (x**2 + y**2) < r**2 

def monte_carlo(n_samples, radius=1):
    """ Return the estimate of pi using the monte carlo method. """
    in_circle_count = 0
    for i in range(n_samples):

        # generate points in the first quadrant
        x = random.uniform(0, radius)
        y = random.uniform(0, radius)

        if in_circle(x, y, radius):
            in_circle_count += 1
    
    estimated_pi = (4 * in_circle_count) / n_samples 

    return estimated_pi 


for n in range(1000, 100001, 10000):
    estimated_pi = monte_carlo(n)
    error = 100 * abs(math.pi - estimated_pi) / math.pi 

    print("Num of samples: {}, Estimated pi: {:.4f},  percentage of error: {:.4f}".format(n, estimated_pi, error))


    