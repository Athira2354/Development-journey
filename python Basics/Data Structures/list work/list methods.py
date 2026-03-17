"""

list is mutable

class list:

def append(self,object)-add object to the end of the list

def insert(self,index,object)

def pop(self,index(default value =-1))=> remove and return specified element at index

def remove(self,object)=>remove first occurance of object

def count(self,object)=>frequency of object in the list

def sort(self,reverse=false)

def extend(self,iterable)
"""
print(dir(list))

colours=["red","green","blue"]

colours.append("yellow")

print(colours)



colours.insert(2,"orange")

print(colours)



removed_element=colours.pop()
print(colours)

removed_element=colours.pop(2)
print(colours)

removed_element=colours.remove("blue")
print(colours)

# removed_element=colours.remove("pink")
# print(colours)

colours=["violet","indigo","blue","red","green","red","violet","blue","red"]

print(colours.count("red"))



ami_fvt_clrs=["red","green","yellow","blue","white"]
aaru_fvt_clrs=ami_fvt_clrs.copy()
# print(aaru_fvt_clrs)
print(ami_fvt_clrs is aaru_fvt_clrs) 

#is operator is an identity operator
                    # returns boolean value
                    # identity operator checks whether two variables are pointing same memory or not
print(ami_fvt_clrs==aaru_fvt_clrs) # true ==value compare
print(ami_fvt_clrs is aaru_fvt_clrs)#false is memory location compare


list=[20,15,18,12,5,10]
list.sort() #sort the elements  in ascending order
print(list)
list=[20,15,18,12,5,10]
list.sort(reverse=True) #sort the elements in descending order
print(list)

list.reverse()
print(list)

colours.reverse()
print("reversed colours=",colours)

colours.sort(reverse=False)
print("solrted colours=",colours)


colours=["white","green","yellow","orange","red"]
new_colours=["cyan","pink","grey"]
colours.extend(new_colours)
print(colours)