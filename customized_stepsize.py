import numpy as np
import matplotlib.pyplot as plt


def search_accelabre_customized_stepsize(s):

    def function(x):
        
        return x * (x - 1.5)

    plt.plot(np.arange(-25, 25), function(np.arange(-25, 25)))
    x = -10
    temp = function(x)
    plt.plot(x,temp,'ro')
    optimal = True
    direction = True
    x = x + s
    list = [0, 0]
    while optimal:
        # sonraki oncekinden boyukdurse
        # Left gedecek
        given = function(x)
        plt.plot(x, given, 'ro')
        if given < temp:
            if direction == True:
                s = s * 2
                x = x + s

            else:
                x = x - s
            temp = given

            print(f"Lets go Left {x} and {given}")

        elif given > temp:

            direction = not direction
            s = s / 2
            plt.plot(x,given,'go')
            if direction == True:
                x = x + s
            else:
                x = x - s
            temp = given
            print(f"Lets go Change Direction to the {direction} {x} and {given}")

        else:
            print(f"Result is in x = {x} and y = {given}")
            break
