import numpy as np


class dischotomous_search:
    """
    Written by Reshad Abdulkhaligov
    In the dichotomous search, two experiments are placed as close as possible at
    the center of the interval of uncertainty. Based on the relative values of the objective
    function at the two points, almost half of the interval of uncertainty is eliminated.
     Parameters
    ----------
    function : function
        Input Objective Function.
    interval : list
        Interval as a list from left to right boundry
    precision : float,
        Floating point precision. It's precision accuracy
        If interval difference is one precision should be different than sigma
    sigma : float,
         δ is a small positive number chosen so that the two experiments give significantly
         different results Default is 0.001


    Returns
    -------
    list : self.opt
            coordinates of  represents optimal point
    """

    def __init__(self, function, interval, precision, siqma=0.001):
        # self.f = function
        self.function = function
        self.interval = interval
        self.precision = precision
        self.sigma = siqma
        self.__step()
        self.opt = []

    def __step(self):
        t = self.sigma / self.interval[1] - self.interval[0]
        self.step = 2 * int(np.log2((1 - t) / (self.precision - t)))

    def run(self):
        L_0 = 0.5 * (self.interval[1] - self.interval[0])
        for i in range(self.step // 2):
            x1 = L_0 - 0.5 * self.sigma
            x2 = L_0 + 0.5 * self.sigma
            if self.function(x1) > self.function(x2):
                self.interval[0] = x1
            elif self.function(x1) < self.function(x2):
                self.interval[1] = x2

            L_0 = self.interval[0] + (self.interval[1] - self.interval[0]) / 2
        self.opt = [np.mean(np.array(self.interval)), self.function(np.mean(np.array(self.interval)))]

        print(f"Optimization Done! Your optimal points are : at x_opt = {self.opt[0]}, f(x_opt) = {self.opt[1]}")

        return self.opt
