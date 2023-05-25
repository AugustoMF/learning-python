command = ""
started = False
while command != quit:
    command = input ("> ").lower()

    if command == "start":

        if started == False:
            print ("Car started")
            started = True
        else:
            print ("You've already started the car, moron!")

    elif command == "stop":

        if started == True:
            print ("car stopped")
            started = False
        else:
            print ("the car is already stopped you idiot!")
    
    elif command == "Help":   
        print ("""
type start to start your car
type stop to stop your car
type quit to quit the game
        """)

    elif command == "quit":
        break

    else: 
        print ("Sorry, I do not understand this command")
