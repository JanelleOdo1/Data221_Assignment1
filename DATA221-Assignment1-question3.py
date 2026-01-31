def compute_exponent_of_numbers(x,y):
    return x ** y

list_of_pairs = [[5, 2], [3, -1], [4, 3], [2,0]]
final_list = []

for x, y in list_of_pairs:
    if y < 0:
        continue
    final_list.append(compute_exponent_of_numbers(x,y))

print(final_list)