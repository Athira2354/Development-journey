head_count=5

bill_amount=250

# add 8 % gst

gst= (8/100)*bill_amount
bill_amount= bill_amount + gst
individual_split= bill_amount/head_count
print(individual_split)


