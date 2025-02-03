# A = P(1 + R/100) t 
# Compound Interest = A – P 


def compound_interest(principal, rate, time): 
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
 
compound_interest(10000, 8, 5)