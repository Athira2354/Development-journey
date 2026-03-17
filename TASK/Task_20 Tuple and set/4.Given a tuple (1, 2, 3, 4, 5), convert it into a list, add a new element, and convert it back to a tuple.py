org_tuple=(1,2,3,4,5)
con_list=list(org_tuple)
con_list.append(6)
new_tuple=tuple(con_list)

print(f'orginal tuple =',org_tuple)
print(f'modified tuple = ',new_tuple)