import pickle
# d=dict(name='zhuiyun',age=19)
# print(pickle.dumps(d))
# try:
#     file=open("d:/序列化.txt","wb")
#     pickle.dump(d,file)
# finally:
#     file.close()

try:
    file=open("d:/序列化.txt","rb")
    print(pickle.load(file))
finally:
    file.close()