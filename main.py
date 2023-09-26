import math
import random

import matplotlib
import timeit
import matplotlib.pyplot as plt
import numpy as np

# Better plots in PyCharm

matplotlib.use("TkAgg")


# Binary search implemented in place

def binary_search(the_list, target_item):
    return binary_search_in_place(the_list, target_item, 0, len(the_list))


# With left and right limits
def binary_search_in_place(the_list, target_item, left, right):
    # How long is the list?

    l = right - left

    # Base cases

    if l == 0:
        return False, 0
    elif l == 1:
        if the_list[left] == target_item:
            return True, left
        else:
            return False, 0
    else:
        # Find the middle

        middle = left + l // 2

        # We have a trichotomy
        # Either in left, in right or we found it

        if target_item < the_list[middle]:
            return binary_search_in_place(the_list, target_item, left, middle)
        elif target_item == the_list[middle]:
            return True, middle
        elif target_item > the_list[middle]:
            return binary_search_in_place(the_list, target_item, middle + 1, right)
        else:
            raise Exception('We shouldn\'t be here')


# Code snippets for timeit

SETUP_CODE = '''
from __main__ import binary_search, my_list, n, target
import random
'''

TEST_CODE = '''
binary_search(my_list, target)
'''

# Enable interactive graphing and create axes

plt.ion()
f = plt.figure()
ax = f.add_subplot(111)

# Lists to receive points

x = []
y = []

x2 = []
y2 = []

# Add plots to axes

sc = ax.scatter(x, y)
plt.sca(ax)
lp = plt.plot(x2, y2)

# Index list length

n = 1

# Rolling average length

size = 10

# Pause between plots

pause = 100

# Loop forever

while True:
    # Find rolling average of times

    times = []

    for _ in range(size):
        # A list to sort and a target to find

        my_list = sorted([random.randint(1, n) for _ in range(n)])
        target = random.randint(1, n)

        # Time the sort

        next_time = timeit.timeit(setup=SETUP_CODE,
                                  stmt=TEST_CODE,

                                  number=4
                                  )

        # Add time to our list

        times.append(next_time)

    # Get the min from our list

    t = min(times)

    # And add to our list to plot

    x.append(n)
    y.append(t)

    # Increment list size

    n += 1

    # Add rolling average to plot

    if n % size == 0:
        x2.append(sum(x[-size:]) / size)
        y2.append(sum(y[-size:]) / size)

        lp = []
        plt.sca(ax)
        plt.plot(x2, y2, color='red')

    # Plot after pause

    if n % pause == 0:
        sc.set_offsets(np.c_[x, y])

        ax.set(xlim=(0, max(x)),
               ylim=(0, max(y))
               )

        f.canvas.draw_idle()
        f.canvas.flush_events()
