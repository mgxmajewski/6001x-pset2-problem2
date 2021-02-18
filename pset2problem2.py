# Paying Debt Off in a Year

# Calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant
# amount that will be paid each month.

# Given input
balance = 3329
annualInterestRate = 0.2
# Expected output "Lowest Payment: 310"

# Declare variables to calculate lowest possible monthly down payment

year_months = 12
monthlyInterestRate = annualInterestRate / year_months
balance_temp = balance

# Value to be found
monthlyPayment = 10

while balance_temp > 0:
    # Calculate monthly interests
    balance_temp -= monthlyPayment
    monthlyPayment += 10


print("Lowest Payment:", round(monthlyPayment, 2))

