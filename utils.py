import numpy as np
import matplotlib.pyplot as plt
import random

# y = mx + b
m = 2
b = 1   
# y = 2x + 1

def sign(n):
    if n > 0:
        return 1
    else:
        return -1

def sample_points(num):
    points = list()
    for i in range(int(num/2)):
        x = random.randint(1,num)
        bias = random.randint(1,num*2)
        y = m * x + b + bias
        label = sign(m * x + b - y)
        points.append([x, y, label])

        x = random.randint(1,num)
        bias = random.randint(1,num*2)
        y = m * x + b - bias
        label = sign(m * x + b - y)
        points.append([x, y, label])

    random.shuffle(points)
    
    return points

def visual(samples,w=[]):
    lx = np.arange(len(samples))
    ly = m * lx + b
    plt.plot(lx, ly, color='g', label='groundtruth')
    for i in range(len(samples)):
        if samples[i][-1] == 1:
            plt.plot(samples[i][0], samples[i][1], 'o', markersize=3, color='blue')
        else:
            plt.plot(samples[i][0], samples[i][1], 'o', markersize=3, color='red')
    if w != []:
        # w0 + w1x + w2y = 0
        # y = -w0/w2 - (w1/w2)x
        if(w[2]==0):
            print('Warning: w[2]=0 -> w = ', w)
        x = lx
        y = -w[0]/w[2] - (w[1]/w[2])*x
        plt.plot(x, y, color='gold', label='pla-answer')
    plt.legend()
    plt.show()