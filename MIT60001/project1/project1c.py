'''
What percent to save to get a downpayment in 36 months
'''

def intput(x):
    return int(input(x))

def floatput(x):
    return float(input(x))

starting_annual_salary = intput("Enter your annual salary: ")
saving_rate = 0
total_cost = 1000000
semi_annual_raise = 0.07

num_steps = 0
portion_down_payment = 0.25*total_cost
current_savings = 0
investment_return = 0.04 #assuming annual rate
best_rate_found = False

high = 10000
low = 0

while not best_rate_found:
    saving_rate = ((high+low)/2.0)/10000
    current_savings = 0
    annual_salary = starting_annual_salary
    
    for num_months in range(36):
        monthly_returns= current_savings*investment_return/12  
        portion_saved = saving_rate*annual_salary/12
        current_savings += monthly_returns+portion_saved
        if num_months>0 and num_months%6 == 0:
            annual_salary += annual_salary*semi_annual_raise
        
    if abs(current_savings-portion_down_payment)<=100:
        best_rate_found = True
        print("Best savings rate:", saving_rate)
        print(f"Steps in bisection search: {num_steps}")
    elif high-low<=1:
        print("It's not possible within 3 years")
        break
    elif current_savings<portion_down_payment:
        low = int(saving_rate*10000)
    elif current_savings>portion_down_payment:
        high = int(saving_rate*10000)
    
    num_steps+=1
    
    