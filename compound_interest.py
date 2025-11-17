# Define variables
principal = 1000   # Principal amount in dollars
rate = 0.05        # Annual interest rate (5%)
time = 3           # Time in years

# Calculate total amount after compound interest
amount = principal * (1 + rate) ** time

# Calculate interest earned
interest = amount - principal

# Print the result
print(f"The compound interest is: {interest}")
