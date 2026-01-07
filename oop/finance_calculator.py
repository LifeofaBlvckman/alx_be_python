# Finance Calculator
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate annual savings with 5% interest
annual_savings = monthly_savings * 12
interest = annual_savings * 0.05
projected_savings = annual_savings + interest

# Display results
print("Your monthly savings are $", int(monthly_savings), ".", sep="")
print("Projected savings after one year, with interest, is: $", int(projected_savings), ".", sep="")
