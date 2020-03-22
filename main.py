from intervalhalving import intervalhalving
import numpy as np
from fibonacci_search import fibonacci_search
from dishotomous_search import dischotomous_search
from golden_section import golden_section
if __name__ == "__main__":
    test = golden_section(lambda x:x*x - 2*x + 1,[0,3],0.0009)
    test.run()
