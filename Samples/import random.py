import random
x=round(random.uniform(6,8), 2)
print(x)

def compound_interest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
    
    print("Total amount is", round(Amount))
    
compound_interest(100000, 7.7, 5)