set={10,20,30,40,50}
#     1  2  3  4  5


for num in set:
    print(num)


colours={"red","green","yellow","orange","blue","hai",1,True}
for c in colours:
    print(c)


# data structure working behind list is array
# data structure working behind set is hash set
"""
class set:
    def add(self,value)
"""
food={"dosa","puri","idli","appam"}

food.add("biriyani")

print(food)


set_a={10,20,30,40,50,60,80}

set_b={10,20,100,200,250,300}

# union
# ----------
u_set= set_a.union(set_b)
print("union=",u_set)

# intersection
# -------------------
i_set= set_a.intersection(set_b)
print("intersection=",i_set)


# difference
# ---------------------------
d_set=set_a.difference(set_b)
print("difference=",d_set)



"""
class set()
    def add(self,value) -adds new object to the set
    def union(self,set)
    def intersetion(self,set)
    def difference()
    def issuperset()-checks whether supperset or no
    def issubset()



set is mutable
 it can only updated with one another set
 set is unorderd
 indexing is not supported


"""