secret = 7
i = 0
j = 3
while i < j:
    a = int(input("guess the number between 1 and 9"))
    i += 1
    if a == secret:
        print("you won")
        break
else:
    print("you lose")       