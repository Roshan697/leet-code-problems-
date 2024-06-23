message = input(">")

words = message.split(' ')
emojis = {":)":"😊", 
          ":(":"🥺"}

output = ""
for word in words:
    output += emojis.get(word) + " "
print(words)

