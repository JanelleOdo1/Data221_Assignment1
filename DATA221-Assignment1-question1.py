threshold = 100
product = 1
currentNumber = 1
while product <= threshold:
    product *= currentNumber
    currentNumber += 1

print(f"Final Product: {product}")
print(f"Integer that caused it to exceed the threshold: {currentNumber}")
