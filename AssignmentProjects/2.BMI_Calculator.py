#Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g.
#If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Warning you should convert the result to a whole number.

# Example Input
# weight = 80
# height = 1.75
# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# Output : 26

#Write your code below

#Type conversion
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in m: "))
#print(type(height))

#Formula - (weight/height**2)
BMI = weight / height**2
#print(BMI)

#BMI smaller than 18.5 is underweight
#BMI between 18.5 and 25 is normal weight
#BMI between 25 and 30 is overweight
#BMI between 30 and 35 is obese
#BMI greater than 35 is clinically obese

BMI = round(weight / height**2)
print(BMI)

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")
