# sales_report={
#     "Sun":12000,
#     "Mon":25000,
#     "Tue":10000,
#     "Wed":18000,
#     "Thu":25000,
#     "Fri":13000,
#     "sat":20000,
# }

# # display day wise sales report
# for key in sales_report:
#     value=sales_report[key]
#     print(key,value)

# # total sale
# for key in sales_report:
#     total_sale=0
#     total_sale+=sales_report[key]
   
# print(total_sale)

# # avg sale
# avg_sale=0
# avg_sale=total_sale/len(sales_report)
# print(avg_sale)

# for key in sales_report:
#     value=sales_report[key]
#     if value<avg_sale:
#         printkey,value)

sales_report={
    "sun":32000,
    "mon":19000,
    "tue":29000,
    "wed":20000,
    "thu":18000,
    "fri":19000,
    "sat":20000,

}
total_sale=0
for key in sales_report:
    print(key,sales_report[key])

    total_sale+=sales_report[key]
print("total sale =",total_sale)    
avg_sale=total_sale/len(sales_report)
print("avrage =",avg_sale)
for key in sales_report:
    if sales_report[key]<avg_sale:
      print("day with low sale =",key,sales_report[key])