employees=["hari","manu","madhav","sanu"]
fw=open("employees.txt","w")
for e in employees:
    fw.write(e+"\n")
print("completed")