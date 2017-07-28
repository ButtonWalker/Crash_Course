for value in range(1, 21):
    print(value)

numbers = []
for value in range(1,1001):
    numbers = value
    print(numbers)

digits = range(1, 1000001)
print(min(digits))
print(max(digits))
print(sum(digits))

# odd numbers
for value in range(1,21,2):
    print(value)

for value in range(3, 30, 3):
    print(value)

cubes = []
for value in range(1, 11):
    cubes.append(value**3)

print(cubes)

cubes = [value**3 for value in range(1,11)]
print(cubes)