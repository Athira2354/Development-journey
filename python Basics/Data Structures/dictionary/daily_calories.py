daily_calories={
                "Mon":1200,
                "Tue":2300,
                "Wed":1500,
                "Tue":1250,
                "Fri":1800,
                "Sat":1450,
                "Sun":1300,

            }
for key in daily_calories:
    print(key,daily_calories[key])

total_calorie=0  #total calorie
for key in daily_calories:
    cal=daily_calories[key]
    total_calorie +=cal
print(total_calorie)
#avg calorie
avg_calorie=total_calorie/len(daily_calories)
print(avg_calorie)