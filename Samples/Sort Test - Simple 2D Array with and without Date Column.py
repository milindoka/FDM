#required for date sort only
from datetime import datetime

print("Sorting simple array")

li=[[3,4,5],
    [1,2,3],
    [5,2,3]]
print("Original Array")    
for x in li :
    print(x)
    
print("Array sorted on column2")   

li.sort(key=lambda x: x[1])
for x in li :
    print(x)

print("Sorting 2D array with date column")
print("Original Arrray")

d=[[1,2,"23/12/19"],
  [3,5,"11/03/17"],
  [5,8,"10/09/18"],
  [3,1,"31/05/18"],
  [4,4,"25/11/19"]]

for x in d :
    print(x)

print("Sorted 2d array with date in column 3")
sorted_d=sorted(d,key=lambda t: datetime.strptime(t[2],'%d/%m/%y'))

for x in sorted_d :
    print(x)



