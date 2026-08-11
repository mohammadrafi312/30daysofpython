# Q18 — Hardest Coding Challenge of Day 1

# Build a Student Result Calculator.

# Take:

# Student name
# Age
# Subject 1 marks
# Subject 2 marks
# Subject 3 marks

# Then display:

# ========== RESULT ==========

# Name       : Rafi
# Age        : 20

# Subject 1  : 87
# Subject 2  : 92
# Subject 3  : 78

# Total      : 257
# Average    : 85.6666666667
# Percentage : 85.6666666667%
# ============================
# Restrictions

# You can use:

# ✅ Variables
# ✅ input()
# ✅ print()
# ✅ int() / float()
# ✅ Arithmetic operators
# ✅ f-strings

# You cannot use:

# ❌ if
# ❌ else
# ❌ elif
# ❌ loops
# ❌ lists
# ❌ dictionaries
# ❌ functions

# 💡 Hint

# You'll need:

# total = mark1 + mark2 + mark3
# average = total / 3
# percentage = ...

# CODE :

student_name =input("enter the student name:")
student_age =int(input("student age :"))
subject1 =int(input("marks of subject 1:"))
subject2 =int(input("marks of subject 2:"))
subject3 =int(input("marks of subject 3:"))
total = (subject1 + subject2 + subject3)
Average =(subject1 + subject2 + subject3/3)
percentage = (total / 300) * 100

# print("===================RESULTS====================")
print(f"name  :{student_name}")
print(f"age   :{student_age}")

print("total:",total)
print("Average:",Average)
print("percentage:",percentage,"%")