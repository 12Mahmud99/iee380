import numpy as np

samples = [np.random.randint(1, 10001) for i in range(20)]

for s in samples:
    is_composite = any(s % i == 0 for i in range(2, int(s**0.5) + 1))
    if is_composite:
        print(f"{s} is composite")
    else :
        print(f"{s} is NOT composite")
print(samples)

###this code checks if the number in the samples list are all
##composite 