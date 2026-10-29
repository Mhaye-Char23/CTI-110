 # Charlette-Mhaye Derewecki
 # 10/28/26
 # P1HW2
 # Basic math on numbers that will be entered

# 3. Ask user to enter their budget
budget = float(input("Enter your total budget: "))

# 4. Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# 5. Ask user for amount they will spend on gas
gas = float(input("Enter amount you will spend on gas: "))

# 6. Ask user for amount they will spend on accommodation
accommodation = float(input("Enter amount you will spend on accommodation: "))

# 7. Ask user for amount they will spend on food
food = float(input("Enter amount you will spend on food: "))

# 8. Add expenses
total_expenses = gas + accommodation + food

# 9. Subtract expenses from budget
remaining_budget = budget - total_expenses

# 10. Display results
print("\n--- Travel Budget Summary ---")
print(f"Destination: {destination}")
print(f"Total Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
