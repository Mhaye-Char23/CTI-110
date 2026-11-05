 # Charlette-Mhaye Derewecki
 # 11/4/26
 # P2HW1
 # A brief description of the project

# Get information from the user
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
fuel_cost = float(input("How much do you think you will spend on gas? "))
accommodation_cost = float(input("Approximately, how much will you need for accommodation/hotel? "))
food_cost = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
remaining_balance = budget - fuel_cost - accommodation_cost - food_cost

# Display results
print()
print("------------Travel Expenses------------")
print(f"{'Location:':<25}{destination}")
print(f"{'Initial Budget:':<25}${budget:.2f}")
print(f"{'Fuel:':<25}${fuel_cost:.2f}")
print(f"{'Accommodation:':<25}${accommodation_cost:.2f}")
print(f"{'Food:':<25}${food_cost:.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':<25}${remaining_balance:.2f}")