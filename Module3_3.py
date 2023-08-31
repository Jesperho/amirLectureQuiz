#Write a program that asks for the biological gender and hemoglobin value (g/l).
#The program then notifies the user if the hemoglobin value is low, normal or high.

#A normal hemoglobin value for adult females is between 117-155 g/l.
#A normal hemoglobin value for adult males is between 134-167 g/l.


gender = input("What is your gender? (F/M)").upper()
hemoglobin = float(input("Enter your hemoglobin value (g/l)"))

if gender == "F":
    if 117<= hemoglobin <= 155:
        result = "Normal"
    elif hemoglobin < 117:
        result = "Low"
    else:
        result = "High"
elif gender == "M":
    if 134<= hemoglobin <= 167:
        result = Normal
    elif hemoglobin <134:
        result = "Low"
    else:
        result = "High"

else:
    result = "Invalid gender"

print(f"The hemoglobin value for {gender} is {result}.")





