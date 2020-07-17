li=[11,22,33,44,55,66,77,88,99,90]
list1=[]
list2=[]
for item in li:
    if item >=66:
        list1.append(item)
    else:
        list2.append(item)
dic={'k1':list1,'k2':list2}
print(dic)