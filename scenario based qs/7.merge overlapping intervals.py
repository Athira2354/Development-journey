intervals=[(1,3),(2,6),(8,10),(9,12)]
intervals.sort()
merged=[]
for start,end in intervals:
 if not merged or  merged[-1][-1]<start:
  merged.append((start,end))
 else:
  prev_start,prev_end=merged[-1]
  merged[-1]=prev_start,max(prev_end,end)
print(merged)