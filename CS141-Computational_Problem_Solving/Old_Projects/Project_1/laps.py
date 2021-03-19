miles = float(input("How many miles would you like to run in miles? "))
track = float(input("how long is the track in miles? "))
laps= miles//track
onemore = laps+1
print("You must run between "+str(laps)+" and "+str(onemore)+" laps")
