'''
How long iwll it take to save enough money for a down payment
'''

def intput(x):
    return int(input(x))

annual_salary = intput("Enter your annual salary: ")
percent_save = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = intput("Enter the cost of your dream home: ")

num_months = 0
portion_down_payment = 0.25*total_cost
current_savings = 0
investment_return = 0.04 #assuming annual rate

while current_savings<portion_down_payment:
    monthly_returns= current_savings*investment_return/12  
    portion_saved = percent_save*annual_salary/12
    current_savings += monthly_returns+portion_saved
    num_months+=1
    
print("Number of months:", num_months)
    