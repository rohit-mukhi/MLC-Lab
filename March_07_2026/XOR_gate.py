# XOR gate using mcp_neuron

def AND(x1, x2):
    return 1 if x1+x2==2 else 0

def OR(x1, x2):
    return 1 if x1+x2==1 else 0

def NOT(x):
    return 0 if x==1 else 1


for x1 in [0, 1]:
    for x2 in [0, 1]:
        xor = AND( OR(x1, x2), NOT(AND(x1, x2)) )
        print(x1, x2, "->", xor)
