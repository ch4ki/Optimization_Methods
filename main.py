from intervalhalving import intervalhalving
from dishotomous_search import dischotomous_search
if __name__ == "__main__":
    test = intervalhalving(lambda x:x*(x - 1.5),[0,1],0.001)
    test.run()
