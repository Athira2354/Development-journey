from csv import DictReader

fr=open("TASK\\Task_28\\move.csv","r")
data=list(DictReader(fr))
print(data)



# Write a Python program to read the file move.csv and print the first 5 rows.