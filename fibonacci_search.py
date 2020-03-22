import numpy as np


class fibonacci_search:
    def __init__(self, function, interval, step_size):
        self.function = function
        self.interval = interval
        self.step_size = step_size
        self.f_numbers = self._fibonacci_n()

    def _fibonacci_n(self):
        fibonacci = [1, 1]
        for i in range(2, self.step_size):
            fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        return fibonacci

    def run(self):
        L_a = (self.f_numbers[self.step_size - 2] / self.f_numbers[self.step_size]) * (
                    self.interval[1] - self.interval[0])
        J = 2
        while J != self.step_size:
            L = self.interval[1] - self.interval[0]
            # To make sure x1 will always be in left
            if L_a > L / 2:
                x1 = self.interval[1] - L_a
                x2 = self.interval[0] + L_a
            else:
                x1 = self.interval[1] + L_a
                x2 = self.interval[0] - L_a

            f1 = self.function(x1)
            f2 = self.function(x2)

            if f1 > f2:
                self.interval[0] = x1
                L_a = (self.f_numbers[self.step_size - J] / self.f_numbers[self.step_size - (J - 2)]) * L
            elif f2 > f1:
                self.interval[1] = x2
                L_a = (self.f_numbers[self.step_size - J] / self.f_numbers[self.step_size - (J - 2)]) * L
            else:
                self.interval[0] = x1
                self.interval[1] = x2
                L_a = (self.f_numbers[self.step_size - J] / self.f_numbers[self.step_size - (J - 2)]) * (
                            self.interval[1] - self.interval[0])
                J += 1
            J += 1
        print(
            f"Optimization Done! Your optimal points are : at f2(x_opt) = {self.interval[0]}, f1(x_opt) = {self.interval[1]}")
