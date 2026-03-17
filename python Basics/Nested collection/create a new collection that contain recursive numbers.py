nums=[10,11,10,11,12,13,14,15,16,15]
recurssive_nums={n for n in nums if nums.count(n)>1 }
print(recurssive_nums)
