fr=open("python Basics\\file\\flight.txt","r")
flight_info=[]
for line in fr:
    data=line.rstrip("\n").split(",")
    passenger_data={"year":data[0],"month":data[1],"passengers":int(data[2])}
    flight_info.append(passenger_data)
year_wise_count={}
for p in flight_info:
    year=p.get("year")
    p_count=p.get("passengers")
    if year in year_wise_count :
        year_wise_count[year]+=p_count
    else:
        year_wise_count[year]=p_count
print(year_wise_count)




# fr=open("python Basics\\file\\flight.txt","r")
# flight=[]
# for line in fr:
#     data=line.rstrip("\n").split(",")
#     dic={"year":data[0],"month":data[1],"passengers":int(data[2])}
#     flight.append(dic)
# year_wise_count={}    
# for p in flight:
#     year=p.get("year")
#     p_count=p.get("passengers")
#     if year in year_wise_count:
#         year_wise_count[year]+=p_count
#     else:
#         year_wise_count[year]=p_count    
# print(year_wise_count)
# year_wise_count_sorted=sorted(year_wise_count,key=year_wise_count.get)
# print(year_wise_count_sorted)