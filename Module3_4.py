year = int(input("Enter a year"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    result = "is a leap year"
else:
    result = "is not a leap year"

print(f"The year {year} {result}")