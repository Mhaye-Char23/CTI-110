# Charlette-Mhaye Derewecki
# 11/18/26
# P4HW1
# Assignment assess student ability to edit and enhance exiting programs

# Get number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Make sure at least two scores are entered
while num_scores < 2:
    print("Please enter at least 2 scores.")
    num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list
score_list = []

# Collect scores
for i in range(num_scores):

    score = float(input("Enter score #" + str(i + 1) + ": "))

    # Validate scores
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")

        score = float(input("Enter score #" + str(i + 1) + " again: "))

    # Add valid score to list
    score_list.append(score)

# Find lowest score
lowest_score = min(score_list)

print()
print("-------------Results-------------")

# Display lowest score
print("Lowest Score  :", lowest_score)

# Remove lowest score
score_list.remove(lowest_score)

# Display modified list
print("Modified List :", score_list)

# Calculate average using running total
total = 0

for score in score_list:
    total += score

average = total / len(score_list)

# Display average
print("Scores Average:", format(average, ".2f"))

# Determine letter grade
if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
else:
    print("Grade: F")