import numpy as np


class golden_section:
    def __init__(self, function, interval, accuracy):
        self.function = function
        self.interval = interval
        self.accuracy = accuracy
        self.step = self.__step()
        self.opt = []
        self.temp = 0

    def __step(self):
        distance = self.interval[1] - self.interval[0]
        return np.ceil(np.log(self.accuracy / distance) / np.log(0.61803))

    def _temp(self, temporary):
        self.temp = temporary

    def run(self):
        global temp
        p = 0.3819
        distance = self.interval[1] - self.interval[0]
        a = self.interval[0] + p * distance

        b = self.interval[0] + (1 - p) * distance

        f1 = self.function(a)
        f2 = self.function(b)

        for i in range(int(self.step)):
            if f1 < f2:
                self.interval[1] = b
                temp = a if i == 0 else self.temp
                a = self.interval[0] + p * (self.interval[1] - self.interval[0])
                f1 = self.function(a)
                self._temp(temp)
                f2 = self.function(self.temp)
            elif f1 > f2:
                self.interval[0] = a
                temp = b if i == 0 else self.temp
                b = self.interval[0] + (1 - p) * (self.interval[1] - self.interval[0])
                self._temp(temp)
                f1 = self.function(self.temp)
                f2 = self.function(b)

        print(self.interval)


