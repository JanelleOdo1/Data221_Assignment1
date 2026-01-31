from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

chosen_indices = []

for i in range(len(values)):
    if values[i] >= x:
        chosen_indices.append(i)

print(f"Sorted list: {values}")
print(f"X: {x}")

if chosen_indices:
    print(f"First matching index: {chosen_indices[0]}")
else:
    print(f"No value is greater than or equal to {x}")