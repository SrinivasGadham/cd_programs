import math

x = 1.0  # Assuming a specific value for x
i = 0
result = math.sin(x) / math.cos(x)  # Compute sin(x)/cos(x) outside the loop

while i < 100:
    a = result + i
    i += 1
