import numpy as np
import matplotlib.pyplot as plt

import random
x = eval(input('請猜1~5的一個號碼'))
y = random.randint(0, 5)
if x == y:
    print('您猜對了，答案正是', x, sep='')
else:
    print('您猜錯了喔～其實是', y, sep='')
