import numpy as np
from utils import *
# from utils import sample_points
# from utils import visual

def PLA(samples):
    w = np.zeros(3,dtype=int)
    count = 0
    while_loop = 0
    while True:
        while_loop = while_loop + 1
        no_mistake = True
        for x in samples:
            x = [1] + x
            x = np.array(x)
            if sign(np.dot(w,x[:-1])) != x[-1]:
                no_mistake = False
                w = w + x[:-1]*x[-1]    # if w = [1 1 0], can it be a line?
                count = count + 1
                # visual(samples,w)
        if no_mistake:
            break;
    print('while_loop = ',while_loop)
    print('count = ',count)
    return w

if __name__ == '__main__': 
    samples = sample_points(30)
    # print(samples)
    w = PLA(samples)
    print('weight w = ',w)
    visual(samples, w)