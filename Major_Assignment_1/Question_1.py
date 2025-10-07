import numpy as np

arr = np.arange(1, 21)
primes = []

def checkPrime(num):
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for val in arr:
    if(checkPrime(val)):
        primes.append(val)

primes = np.array(primes)

mean = np.mean(primes)
variance = np.var(primes)

print(f"The primes between 1-20 are: {primes}")
print(f"The average of primes is: {mean}")
print(f"The variance of primes is: {variance}")
