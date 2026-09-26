# Get the user input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
#z = round(x + y) # input: 4.8 -> output: 5

#print(f"{z:,}") # input: 1000 -> output: 1,000

# Calculate the result and round to 2 decimal places
#z = round(x / y, 2)
z = x / y
print(f"{z:.2f}") # print the result and round to 2 decimal places