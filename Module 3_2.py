cabin_class = input("Which cabin class would you like to choose? (A,B,C,LUX)").upper()

if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: Above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("Windowless cabin above the car deck.")
elif cabin_class == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class")






