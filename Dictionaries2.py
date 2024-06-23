phone = input("phone: ")

digits_mapping = {"1": "one", "2": " two", "3": "three", "4": "four"}

output = " "
for i in phone:
    output += digits_mapping.get(i)
print(output)   
    