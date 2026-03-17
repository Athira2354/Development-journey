manali={
    "arun":1200,
    "abhay":1000,
    "amal":1500,
    "akhil":2000,
    "akshay":800,
    "gokul":2500,
    "abhi":800,
}
total_exp=0
for v in manali.values():
    total_exp+=v
print("total_expense=",total_exp)
indivi_split=round(total_exp/len(manali))
print(indivi_split)
spend_wise={}
for k,v in manali.items():
    payment=indivi_split-v
    spend_wise[k]=payment
print(spend_wise)