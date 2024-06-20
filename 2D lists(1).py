# WAP TO REMOVE DUPLICATE NUMBERS FROM THE LISTS

num = (2,2,4,6,3,4,6,1)
uniques = []

for i in num:
    if i not in uniques:
        uniques.append(i)

print(uniques)

