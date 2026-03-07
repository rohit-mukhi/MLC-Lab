# Nand gate using MCP_Neuron

def mcp_neuron(x1, x2, w1=-1, w2=-1, threshold=-1):
    y_sum = x1 * w1 + x2 * w2
    return 1 if y_sum >= threshold else 0

for x1 in [0, 1]:
    for x2 in [0, 1]:
        print(x1, x2, "->", mcp_neuron(x1, x2))
