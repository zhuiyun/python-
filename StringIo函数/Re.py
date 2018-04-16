#生成文件
import os

# file=open("d:/复习.txt","w")
# #写入文字
# file.write("hello\nworld,\nhi\nzhuiyun")
#读取内容
# file=open("d:/复习.txt","r")
# print(file.read())
#遍历循环1
# for line in file:
#     print(line)

#遍历循环2
# while True:
#     chars=file.readline()
#     if not chars:
#         break
#     print(chars)

#重命名
# open("d:/复习.txt","w")
# os.rename("d:/复习.txt","d:/复习1.txt")

# 序列化
import pickle

d=dict(name="zhuiyun",age=18)
print(pickle.dumps(d))

file=open("d:/小序列化.txt","wb")
pickle.dump(d,file)
file=open("d:/小序列化.txt","rb")
print(pickle.load(file))

print(open("d:/复习1.txt","r").readlines())


