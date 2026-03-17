"""
Task:
- Ask for monthly income

If income ≥ 25,000:
    - Ask for credit score
    - If credit score ≥ 700:
        "Loan approved"
    - Else:
        "Low credit score"
Else:
    "Income not sufficient"


"""
monthly_income=int(input("enter the monthly income: "))

if monthly_income>=25000 :
    credit_score=int(input("enter the credit score: "))
    if credit_score>=700:
        print("loan approved")
    else:
        print("low credit score")
else:
    print("Income not sufficient")
