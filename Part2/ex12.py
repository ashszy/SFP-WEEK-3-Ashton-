# TODO:
# Create a function called check_string that takes one string argument
# If the string starts with the letters "The", return "Found it!"
# Otherwise, return "Nope."

# Insert your code here
def check_string(string_argument) :
    if string_argument.startswith('The') :
        return "Found it!"
    if not string_argument :
        return "Nope."

# Test cases
str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'

print(check_string(str1))    # ➜ Found it!
print(check_string(str2))    # ➜ Nope.
print(check_string(str3))    # ➜ Found it!