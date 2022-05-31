height_cm = int(input("How tall are you? "))

if height_cm >= 140:
    print("You can enter. Have fun!")

elif 140 > height_cm > 119:
    adult = int(input("Are you accompanied by an adult? 1 - Yes  0 - No "))
    if adult == 1:
       print("You can enter with the adult. Have Fun!")
    else:
        print("You can't enter. Sorry.")

else:
    print("You can't enter. Sorry.")