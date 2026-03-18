from csv import DictReader

fr=open("TASK\\Task_28 movie file handling\\move.csv")
data=list(DictReader(fr))
# print(data)



# 1 Write a Python program to read the file move.csv and print the first 5 rows.

for i in range(5):
    print(data[i])

# 2. Write a program to count how many movie records are present in move.csv (excluding the header).
print("total movie records= ",len(data))

# 3.Write a program to read the header row from move.csv and print all column names.
reader = DictReader(fr)
print(reader.fieldnames)



# 4.Accept a year from the user and display all movie titles released in that year from move.csv.

year= input(" enter a year :")

for row in data:
    if row["Year of Release"]==year:
        print(row["Name"])

# Read move.csv and print the movie with the highest rating.

highest_rating=0
top_rated_movie=""
for movie in data :
    if float(movie["Rating"])>highest_rating:
        highest=float(movie["Rating"])
        top_rated_movie=movie["Name"]

print("Movie with highest rating:", movie)
print("Rating:", highest)