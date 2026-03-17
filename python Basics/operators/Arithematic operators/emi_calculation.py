"""
EMI CALCULATION
-----------------------------------------------
INPUT:Princple_amount,Rate_of_interest,No_of_months

EQUATION= EMI=[P x R x (1+R)^N]/[(1+R)^N-1]
OUTPUT:EMI amount

"""
p_amount=350000
rate_of_interest=10
no_of_months=24
R=rate_of_interest/(12*100)
Emi=(p_amount*R*(1+R)**no_of_months)//((1+R)**no_of_months-1)
print("the Emi amount is",Emi,"RS")