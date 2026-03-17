# """
# w.a.p to display least positive missing integer from list with +ve numbers

# sample input1:
#     lst=[1,2,3,5]

#     o/p => 4

# sample input2:
#     lst=[2,3,4,5]

#     o/p => 1

# sample input3:
#     lst=[1,2,3,4,5]
#     o/p=>6



# """
# list=[1,2,3,5]#------------------------
#                 #                     |  

# length=len(list) #4                    |

# for i in range(1,length+1):
#     if i not in list:
#         print(i,"is missing") #4 is missing
#         break     #------------------- |
# else: #  if any this is not missing
#     print(length+1,"is missing")#-------------elemnts in list are include then it return num+1 is =6 is missng




# list=[1,2,3,4,5]
# prev=0
# next=prev+1

# while(prev<length(list)-2):
#     difference=


