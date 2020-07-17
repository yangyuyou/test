li=["alec"," aric","Alex","Tony","rain"]
tu=("alec"," aric","Alex","Tony","rain")
dic={'k1':"alex",' k2':'aric',"k3":"Alex","k4":"Tony"}
li_new=[]
li_aAc=[]
tu_new=[]
tu_aAc=[]
dic_new={}
dic_aAc={}
for i in li:
    k=i.strip()
    li_new.append(k)
    if k.startswith("a") or k.startswith("A"):
        if k.endswith("c"):
            li_aAc.append(k)
        else:
            continue
print("-----------------------")
print("原始数据{}".format(li))
print(li_new)
print(li_aAc)

for i in tu:
    k=i.strip()
    tu_new.append(k)
    if k.startswith("a") or k.startswith("A"):
        if k.endswith("c"):
            tu_aAc.append(k)
        else:
            continue
print("-----------------------")
print("原始数据{}".format(tu))
print(tuple(tu_new))
print(tuple(tu_aAc))

for index_i,i in dic.items():
    k=index_i.strip()
    j=i.strip()
    dic_new[k]=j
    if j.startswith("a") or j.startswith("A"):
        if j.endswith("c"):
            dic_aAc[k]=j
print("-----------------------")
print("原始数据{}".format(dic))
print(dic_new)
print(dic_aAc)
