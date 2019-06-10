dic1 = {1:2,2:3,3:4}
dic2 = {4:5,5:6,7:8,6:7}
dic4 = {}
for d in (dic1,dic2):
    dic4.update(d)
print(dic4)
m = 1
for (l) in dic4.values():
    l = m*l
    #n= m*n
    print(l)
print(l)
print(max(dic4),min(dic4))
print(sorted(dic4.values()))
list1 =[1,2,3,4,5]
list2 = [3,4,5,6,7]
dic5 = dict(zip(list1,list2))
print(dic5)
