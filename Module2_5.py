talent_to_pound = 20
pound_to_lots = 32
lots_to_grams = 13.3

talents = float(input("Enter mass in talents:"))
pounds = float(input("Enter mass in pounds:"))
lots = float(input("Enter mass in lots:"))

total_lots = lots + (pounds + talents * talent_to_pound) * pound_to_lots
total_grams = total_lots * lots_to_grams
total_kilograms = total_grams // 1000
remaining_grams = total_grams % 1000

print(f"The mass is equivalent to {total_kilograms} kilograms and {remaining_grams:.0f} grams.")