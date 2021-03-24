import numpy as np
import time
from utils import *
from q2 import PLA

def count_error(samples, w):
    count = 0
    for x in samples:
        x = [1] + x
        x = np.array(x)
        if sign(np.dot(w,x[:-1])) != x[-1]:
            count = count + 1
    # print('error point number = ', count)
    return count

def find_error(samples, w):
    error_points = []
    for x in samples:
        x = [1] + x
        x = np.array(x)
        if sign(np.dot(w,x[:-1])) != x[-1]:
            error_points.append(x)
    return error_points

def pocket_algorithm(samples):
    w = np.zeros(3,dtype=int)
    best_w = w
    while_loop = 0
    while True:
        while_loop = while_loop + 1
        error_points = []
        error_points = find_error(samples, w)
        if error_points == []:
            break
        x = random.choice(error_points)
        w = w + x[:-1]*x[-1]
        if count_error(samples,w) < count_error(samples,best_w):
            best_w = w
            # print('update best w = ',best_w)
            # visual(samples,best_w)
    print('while loop = ', while_loop, '\niteration = ', while_loop-1)
    return best_w

samples = sample_points(2000)
# visual(samples)
print('------------------PLA------------------')
time_start = time.time() # start timing
w_pla = PLA(samples)
time_end = time.time()    # end timing
time_c= time_end - time_start   # execution time
print('execution time = ', time_c, 's')
# visual(samples,w_pla)

print('------------Pocket Algorithm------------')
time_start = time.time()
w_pocket = pocket_algorithm(samples)
time_end = time.time()
time_c= time_end - time_start
print('execution time = ', time_c, 's')
# visual(samples,w_pocket)

visual(samples,w_pla)
visual(samples,w_pocket)