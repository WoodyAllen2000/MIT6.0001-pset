annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percentage of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream house: '))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
number_months = 0
mr = r/12
payment = portion_down_payment*total_cost
while current_savings < payment:
    current_savings = current_savings*(1 + mr) + monthly_salary*portion_saved
    number_months += 1
print('number of months', number_months)

