from customized_stepsize import *
from dishotomous_search import dischotomous_search
if __name__ == "__main__":
    test = dischotomous_search(lambda x:x*(x - 1.5),[0,1],0.01,0.0001)
    test.run()
