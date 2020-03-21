"""
Stopwatch program
"""

import time

start_click = time.time()

tmp = 0
for i in range(400000):
    """
    just to demonstrate how much time has elapsed running this loop
    """
    tmp += i

end_click = time.time()

total = (end_click - start_click)*1000
print(f'time elapsed: {total} milliseconds')