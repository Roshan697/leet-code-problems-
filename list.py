#largest numbers

numbers = [3,6,4,8,10]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number

print(max)        