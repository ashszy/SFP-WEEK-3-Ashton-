# num1 and num2 are integers
num1 = 100
num2 = 2

# num3 and num4 are strings
num3 = int(50)
num4 = int(5)

# TODO: Fix the data type issue below
# Convert string variables to the correct type so the math works
# Insert your code here

# This will work fine
print(int(num1) / int(num2))

# This will cause an error — do NOT change this line!
num5=num3 / num4
num5 = str(num5)
print(num5)