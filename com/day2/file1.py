f=open("test/test.txt",mode="r",encoding="utf-8")
for i in f:
    if not i.strip().startswith("#"):
        print(i)
f.close()

#file.read()#按字节读取
#file.readline()#按行读取
#file.