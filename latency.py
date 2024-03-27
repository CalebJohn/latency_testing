import time
import random
import os
import json

"""
This script measures the latency of the keyboard input by prompting the user for a 
keypress at a random interval between 1 and 3 seconds. The latency is measured as the
time between the prompt and the keypress. The script repeats this process 11 times and
prints the mean, median, max, and min latency.

This is not sufficient for measuring absolute latency. But is useful for comparing
relative latency between different systems (QMK configurations in my case).

"""

delays = []
try:
    for i in range(50):
        time.sleep(random.random() * 1.5 + 1)
        start = time.perf_counter()
        os.system('read -n 1 -s -r -p "Press any key "')
        delay = time.perf_counter() - start
        print(delay)
        delays.append(delay)

        if (i+1) % 10 == 0:
            os.system('read -n 1 -s -r -p "Take a quick break, press a key when you\'re ready to continue "')
            print()

except KeyboardInterrupt:
    pass

delays = [d for d in delays if d > 0.1 and d < 0.4]

mean = sum(delays) / len(delays)
bucketed = [round(d, 2) for d in delays]

# This is the formula for variance of sample, rather than
# variance of a population
variance = sum([(x - mean) ** 2 for x in delays]) / (len(delays) - 1)
print("\nmean:     ", mean)
print("median:   ", sorted(delays)[len(delays) // 2])
print("mode:     ", max(set(bucketed), key=bucketed.count))
print("std. dev.:", variance ** 0.5)
print("max:      ", max(delays))
print("min:      ", min(delays))

