

tips_data = [
    {"total_bill": 16.99, "tip": 1.01, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.34, "tip": 1.66, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 21.01, "tip": 3.50, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 3},
    {"total_bill": 23.68, "tip": 3.31, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 24.59, "tip": 3.61, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 25.29, "tip": 4.71, "sex": "Male",   "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 8.77,  "tip": 2.00, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 26.88, "tip": 3.12, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 4},
    {"total_bill": 15.04, "tip": 1.96, "sex": "Male",   "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 14.78, "tip": 3.23, "sex": "Female", "smoker": "Yes", "day": "Sun",  "time": "Dinner", "size": 2},
    {"total_bill": 10.27, "tip": 1.71, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 35.26, "tip": 5.00, "sex": "Female", "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 15.42, "tip": 1.57, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 18.43, "tip": 3.00, "sex": "Male",   "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 14.83, "tip": 3.02, "sex": "Female", "smoker": "No",  "day": "Sat",  "time": "Dinner", "size": 2},
    {"total_bill": 21.58, "tip": 3.92, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Dinner", "size": 2},
    {"total_bill": 10.33, "tip": 1.67, "sex": "Female", "smoker": "No",  "day": "Fri",  "time": "Lunch",  "size": 2},
    {"total_bill": 16.29, "tip": 3.71, "sex": "Male",   "smoker": "Yes", "day": "Fri",  "time": "Lunch",  "size": 3},
    {"total_bill": 13.37, "tip": 2.00, "sex": "Female", "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 12.69, "tip": 2.31, "sex": "Male",   "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 17.92, "tip": 4.08, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 20.29, "tip": 2.75, "sex": "Female", "smoker": "Yes", "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 15.77, "tip": 2.23, "sex": "Male",   "smoker": "No",  "day": "Thur", "time": "Lunch",  "size": 2},
    {"total_bill": 39.42, "tip": 7.58, "sex": "Male",   "smoker": "Yes", "day": "Sat",  "time": "Dinner", "size": 4},
    {"total_bill": 19.82, "tip": 3.18, "sex": "Female", "smoker": "No",  "day": "Sun",  "time": "Dinner", "size": 2}
]

# Observe the dataset and create your own set of questions based on it.

# 1.What is the average tip amount overall?


avg_tip=sum(di["tip"] for di in tips_data)/len(tips_data)
print(avg_tip)

# 2.What is the average tip percentage

avg_tip_percentage= sum((di["tip"]/di["total_bill"])*100 for di in tips_data)//len(tips_data)
print( f'avg tip percentage={avg_tip_percentage}')

#3. Which day generates the highest total revenue (total_bill)?


revenue_by_day={}

for d in tips_data:
    revenue_by_day[d["day"]]=revenue_by_day.get(d["day"],0)+d["total_bill"]
    max_day=max(revenue_by_day,key=revenue_by_day.get)
print(max_day)
print(f'{revenue_by_day[max_day]}')

# 4.Do smokers tip more on average than non-smokers?

smoker_tips = [d["tip"] for d in tips_data if d["smoker"] == "Yes"]
non_smoker_tips = [d["tip"] for d in tips_data if d["smoker"] == "No"]

avg_smoker_tip = sum(smoker_tips) // len(smoker_tips)
avg_non_smoker_tip = sum(non_smoker_tips) // len(non_smoker_tips)

print(f' avg_smoker_tips= {avg_smoker_tip}')
print(f' avg_non_smoker_tips = {avg_non_smoker_tip}')


# What is the average total bill by gender?
bill_by_gender = {}

for d in tips_data:
    gender = d["sex"]
    bill_by_gender.setdefault(gender, []).append(d["total_bill"])

avg_bill_by_gender = {
    gender: sum(bills)//len(bills)
    for gender, bills in bill_by_gender.items()
}

print(f'avg_bill_by_gender={avg_bill_by_gender}')


# Which meal time (Lunch or Dinner) has higher and average tip percentage?

tips_percentage_by_time={}

for d in tips_data:
    time=d["time"]
    tip_percentage=d["tip"]/d["total_bill"]
    tips_percentage_by_time.setdefault(time,[]).append(tip_percentage)
avg_tips_percentage_by_time={
    time:sum(vals)/len(vals)*100 
    for time,vals in tips_percentage_by_time.items()
    }
print(f'average tip prcentage ny time ={avg_tips_percentage_by_time}')



# Which customer gave the highest tip percentage?/


max_tip_record = max(tips_data,key=lambda d: d["tip"] / d["total_bill"])

print(f'customer={max_tip_record}')


# What percentage of customers are smokers?
smoker_count=len([d for d in tips_data if d["smoker"]=="Yes"])
smoker_percentage=(smoker_count/len(tips_data)*100)

print(f'customer percentage as smoker = {smoker_percentage} %')