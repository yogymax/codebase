
val = [1,23,34,45,5]
v=val.pop()
print(val,v)

import sys
sys.exit(0)



listv = [11,223,41,14,15,31,31,31,31,33,32,33,33,22]
values = set(listv)

for item in listv:
    print(item , listv.count(item))

print(listv)
print(values)

import sys
sys.exit(0)

#
val1 = {1,5,2,3,4}
val2 = {1,22,2,44,3}



result= val1.union(val2)


print(val1)
print(val2)
print(result)

import sys
sys.exit(0)

values  = {20,30,"A","ABC","AB",20,330,}
print(values)




val1 = [10,230,4,"A",[100,200]]# 1 -- 5 3-int  A-str  1-list -- 2 int
val2 = val1.copy()

num=1
print(id(num),num.__sizeof__()) #18240144 18        60248720 24


num=10
str='A'

tup = (10,20,30,[10,20])
#list-- we can perform any operation as long == no change in tuple
lis = [10,20,30,(100,200)]
#list--