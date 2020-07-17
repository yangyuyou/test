from pip._vendor.distlib.compat import raw_input

file=raw_input("请输入文件名：")
f=open("test/test.txt",mode="r",encoding="utf-8")
while True:
    a=0
    for i in range(10):
        b=f.readline()
        if b:
            a+=1
            print(b)
    if a<10:
        print("\n file over!")
        break
    choice=raw_input("是否继续阅读？[Y(yes),N(no)]:").upper()
    if choice=="N":
        break
f.close()


