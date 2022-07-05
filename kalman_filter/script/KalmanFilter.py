from math import *
from time import sleep
import matplotlib.pyplot as plt
import numpy as np

# gaussian function
def f(mu, sigma2, x):
    ''' f takes in a mean, squared variance, input x and returns the gaussian value '''
    coefficient = 10.0 / sqrt(2.0*pi*sigma2)
    exponential = exp(-0.5*(x-mu)**2/sigma2)
    return coefficient * exponential

# update function
def update(mean1, var1, mean2, var2):
    new_mean = (mean1 * var1 + mean2 * var2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

# motion predict/update function
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2

    return[new_mean, new_var]

def main():
    motions = [1, 2, 3, 1, 2, 3, 2, 2, 1, 1]
    measurements = [5, 6, 7, 7.6, 8, 10, 11, 11.2, 14, 13.4]

    # initial parameters
    measurement_sig = 4.
    motion_sig = 2.
    mu = 0.
    sig = 10000.

    for n in range(len(measurements)):
        mu, sig = update(mu, sig, measurements[n], measurement_sig)
        print('Update: [{}, {}]'.format(mu, sig))
        mu, sig = predict(mu, sig, motions[n], motion_sig)
        print('Predict: [{}, {}]'.format(mu, sig))

        x_axis = np.arange(-30, 30, 0.1)
        # create a corresponding list of gaussian values
        g = []
        for x in x_axis:
            g.append(f(mu, sig, x))

        # plot the result 
        plt.plot(x_axis, g)
        plt.pause(0.1)

    plt.show()
    print('\n')
    print('Final result: [{}, {}]'.format(mu, sig))

    # ## Print out and display the final, resulting Gaussian 
    # # set the parameters equal to the output of the Kalman filter result
    # mu = mu
    # sigma2 = sig

    # # define a range of x values
    # x_axis = np.arange(-20, 30, 0.1)

    # # create a corresponding list of gaussian values
    # g = []
    # for x in x_axis:
    #     g.append(f(mu, sigma2, x))

    # # plot the result 
    # plt.plot(x_axis, g)
    # plt.show()

    # # display the *initial* gaussian over a range of x values
    # # define the parameters
    # mu = 0
    # sigma2 = 10000

    # # define a range of x values
    # x_axis = np.arange(-300, 300, 0.1)

    # # create a corresponding list of gaussian values
    # g = []
    # for x in x_axis:
    #     g.append(f(mu, sigma2, x))

    # # plot the result 
    # plt.plot(x_axis, g)
    # plt.show()



if __name__ == "__main__":
    main()