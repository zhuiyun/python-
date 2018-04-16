# try:
#     # open("XXX.txt")
#     # print(num)
#     print("1111111111")
# except  (NameError,IOError) as a:
#     print(a)
# except Exception as y:
#     print("exception")
# else:
#     print("没有异常")
# finally:
#     print("最终执行")
class ShortInputException(Exception):
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast

    def __str__(self):
        return "最少输入三位字符"


def main():
    try:
        s=input("请输入内容:")
        if len(s)<3:
            raise  ShortInputException(len(s),3)
    except ShortInputException as result:
        print(result)
    else:
        print("没有异常")

main()