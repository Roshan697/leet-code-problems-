def emoji_convertor(message):
    words = message.split(' ')
    emojis = {":)": "😊", ":(": "🥺"}

    output = ""
    for word in words:
        output += emojis.get(word, word) + " "  # Provide the word itself if no emoji is found
    return output.strip()  # Remove trailing space

message = input(">")
print(emoji_convertor(message))
