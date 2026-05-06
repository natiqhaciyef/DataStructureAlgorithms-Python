# Arrays are mutable
names = ["John", "Michael", "David", "Oliver", "Ramses", "Huntai"]
for name in names:
    print(name)

print(names[0]) # from start
print(names[-2]) # from back

numbers = [1, 2, 3, 4, 5, 6]
numbers.append(7)
print(numbers)

numbers.insert(2, 11)
numbers.insert(0, -1)  # adds to the givenIndex of list
numbers.insert(-11, -9)  # adds to the first index of list
numbers.insert(20, 19) # adds to the end of the list
print(numbers)
print("-----------------")
numbers.remove(3)
print(numbers)

print(12 in numbers)
print(len(numbers)) # gives length of list
print("-----------------")

for char in "salam":
    print(char)

print("-----------------")
currentRange = range(0, len(numbers))
for index in currentRange:
    print(f"{index} = {numbers[index]}")