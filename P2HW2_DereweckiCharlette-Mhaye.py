# Charlette-Mhaye Derewecki
# 11/4/26
# P2HW2
# Assignment assess student understanding of Lists


# Step 1: Ask the user to enter grades
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Step 2: Store grades in a list
grades = [module1, module2, module3, module4, module5, module6]

# Step 3: Calculate results
lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average_grade = sum(grades) / len(grades)

# Step 4: Display results
print()
print("------------Results------------")
print(f"{'Lowest Grade:':<20} {lowest_grade}")
print(f"{'Highest Grade:':<20} {highest_grade}")
print(f"{'Sum of Grades:':<20} {sum_of_grades}")
print(f"{'Average:':<20} {average_grade:.2f}")