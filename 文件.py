# path="d:/test3.txt"
# fileName=open(path,"w")
# fileName.write("zhuiyun ,hi")
# fileName=open(path,"r")
# print(fileName.read(100))
# fileName=open(path,"a")
# fileName.write("world")
# fileName=open(path,"r")
# print(fileName.read())
# fileName.close()
#
import fileinput
import os


# open("d:/test4.txt","w").write("zhuiyun\nfsdgsdgs\nfdsgfsdgsd\nworld")
fileName=open("d:/test4.txt","r")
# chars=fileName.read(1)
# while chars:
#     print(chars)
#     chars=fileName.read(1)
#
# fileName.close()
#
# for line in fileinput.input("d:/test4.txt"):
#     print(line)

for name in fileName:
    print(name)

# fileName.close()



