# This program rolls a die 1000 times and prints how many times a number occured

import numpy as np

count = 0
outcome = 0
arr = np.array([0, 0, 0, 0, 0 , 0, 0])
# print(arr)
while count<1000: 
    val = np.random.randint(1, 7)
    arr[val] = arr[val] + 1
    count = count + 1

print("Upon rolling the die 1000 times")
print("")
count = 1
while(count <= 6):
    print(f"{count} occured {arr[count]} times")
    count = count + 1
    
# The above code is OP's code, below is sir's code :-)

# rolls = np.random.randint(1, 7, 1000)
# discs = {i: np.sum(rolls == i) for i in range(1, 7)}
# print(discs)
