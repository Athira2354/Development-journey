fr=open("python Basics\\file\\foodlogs.txt","r")
food_logs=[]
for line in fr:
#    1,break_fast,idly,175,11-1-2025,hari
   data = line.rstrip("\n").split(",")
   log={"id":data[0],"meal_type":data[1],"name":data[2],"calories":data[3],"date":data[4],"owner":data[5]}
   food_logs.append(log)
   
print(food_logs)