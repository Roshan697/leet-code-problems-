com = ""
while com.lower() != "quit":
    com = input("> ")
    if com.lower() == "start":
        print("car started...")
    elif com.lower() == "stop":
        print("car stopped...")  
    elif com == "help":
        print("""
        start - to start the car
        stop - to stop the car 
        quit - to quit""")
    else:
        print("command invalid")         




