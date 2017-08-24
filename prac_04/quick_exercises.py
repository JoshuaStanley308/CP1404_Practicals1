numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
print("""The first number is, {}.
The last number is, {}.
The smallest number is, {}.
The largest number is,{}.
The average of the numbers is, {}.""".format(numbers[0], numbers[-1], min(numbers),max(numbers), sum(numbers) / len(numbers)))

