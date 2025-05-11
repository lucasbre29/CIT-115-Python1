# Lucia's Grade Analyzer


#  1: Prompt for the student's name
str_StudentName = input("Name of the person that we are calculating the grades for: ")

#  2: The four test scores as whole numbers
try:
    int_Grade1 = int(input("Enter Test 1: "))
    int_Grade2 = int(input("Enter Test 2: "))
    int_Grade3 = int(input("Enter Test 3: "))
    int_Grade4 = int(input("Enter Test 4: "))
except ValueError:
    print("Please enter valid integer grades.")
    raise SystemExit

#  4: Negative Score
if int_Grade1 < 0 or int_Grade2 < 0 or int_Grade3 < 0 or int_Grade4 < 0:
    print("Test scores must be greater than 0.")
    raise SystemExit

#  3: Lowest Grade dropped
str_DropLowest = input("Do you wish to Drop the Lowest Grade? (Y/N): ").upper()

# 5: Validate input
if str_DropLowest not in ("Y", "N"):
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

#  6: Process
int_Total = 0
int_Count = 4  # Default Grades

if str_DropLowest == "Y":
    # Manual logic to find and drop the lowest (no min, no list)
    if int_Grade1 <= int_Grade2 and int_Grade1 <= int_Grade3 and int_Grade1 <= int_Grade4:
        int_Total = int_Grade2 + int_Grade3 + int_Grade4
    elif int_Grade2 <= int_Grade1 and int_Grade2 <= int_Grade3 and int_Grade2 <= int_Grade4:
        int_Total = int_Grade1 + int_Grade3 + int_Grade4
    elif int_Grade3 <= int_Grade1 and int_Grade3 <= int_Grade2 and int_Grade3 <= int_Grade4:
        int_Total = int_Grade1 + int_Grade2 + int_Grade4
    else:
        int_Total = int_Grade1 + int_Grade2 + int_Grade3
    int_Count = 3  # Dropped one grade
else:
    int_Total = int_Grade1 + int_Grade2 + int_Grade3 + int_Grade4
    int_Count = 4

#  7: Calculate Average
flt_Average = float(int_Total) / int_Count

# 8: Letter Grades
str_LetterGrade = ""

if flt_Average >= 97.0:
    str_LetterGrade = "A+"
elif flt_Average >= 94.0:
    str_LetterGrade = "A"
elif flt_Average >= 90.0:
    str_LetterGrade = "A-"
elif flt_Average >= 87.0:
    str_LetterGrade = "B+"
elif flt_Average >= 84.0:
    str_LetterGrade = "B"
elif flt_Average >= 80.0:
    str_LetterGrade = "B-"
elif flt_Average >= 77.0:
    str_LetterGrade = "C+"
elif flt_Average >= 74.0:
    str_LetterGrade = "C"
elif flt_Average >= 70.0:
    str_LetterGrade = "C-"
elif flt_Average >= 67.0:
    str_LetterGrade = "D+"
elif flt_Average >= 64.0:
    str_LetterGrade = "D"
elif flt_Average >= 60.0:
    str_LetterGrade = "D-"
else:
    str_LetterGrade = "F"

#  13–14: Output
print("\nGrade Summary for", str_StudentName)
print("Test Average is:", format(flt_Average, ".1f"))
print("Letter Grade for the Test is:", str_LetterGrade)













