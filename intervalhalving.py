import numpy as np


class intervalhalving:
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
            Default = 0.001
            Floating point precision. It's precision accuracy
            If interval difference is one precision should be different than sigma
            Precision should be less than 30 to to work better

        Returns
        -------
        list : self.opt
                coordinates of  represents optimal point
    """
    def __init__(self, function, interval, precision=0.001):
        self.function = function
        self.interval = interval
        self.precision = precision
        self.__step()
        self.opt = []

    def __step(self):
        t = np.ceil(1 - 2 * np.log2(2 * self.precision))
        if t % 2 == 0:
            t += 1
        self.step = t

    def run(self):
        interval = [self.interval[0], np.array(self.interval).mean(), self.interval[1]]
        for i in range(int(self.step - 1) // 2):

            quarter = 0.25 * (interval[2] - interval[0])
            x1 = interval[0] + quarter
            x2 = interval[0] + 3 * quarter
            f1 = self.function(x1)
            f2 = self.function(x2)
            f0 = self.function(interval[1])

            if f2 > f0 > f1:
                interval[2] = interval[1]
                interval[1] = x1
            elif f1 > f0 > f2:

                interval[0] = interval[1]
                interval[1] = x2

            elif f1 > f0 and f2 > f0:
                interval[0] = x1
                interval[2] = x2

        self.opt = [interval[1], self.function(interval[1])]
        print(f"Optimization Done! Your optimal points are : at x_opt = {self.opt[0]}, f(x_opt) = {self.opt[1]}")
        return self.opt
