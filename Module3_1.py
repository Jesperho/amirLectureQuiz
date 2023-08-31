
size_limit = 42
zander_length = float(input("Enter the length of the caught zander in centimeters: "))

if zander_length >= size_limit:
    print("Congratulations! The zander meets the size limit.")
else:
    difference = size_limit - zander_length
    print(f"The zander is {difference:} centimeters below the size limit.")
    print("Release the fish back into the lake.")