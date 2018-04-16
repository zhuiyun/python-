card_info=[]


def show_card():
    global card_info
    print("微信:\tQQ\t")
    for i in card_info:
        print("%s\t%s"%(i['wx'],i['qq']))



def main():
    if __name__ == '__main__':
        read_file_data()
        while True:
            print("1.添加名片")
            print("2.修改名片")
            print("3.删除名片")
            print("4.显示名片")
            print("5.退出名片")
            choice=input("输入序号")
            if(choice.isalnum()):
                choice=int(choice)
                if choice==1:
                    add_card()
                elif choice==2:
                    print("修改名片")
                elif choice == 3:
                    print("删除名片")
                elif choice == 4:
                    show_card()
                elif choice == 5:
                    print("修改名片")
                else:
                    print("输入有误")
                    continue
            else:
                print("输入有误")
                continue

def add_card():
    global card_info
    print("*****添加名片*****")
    weixin=input("输入微信号")
    qq=input("输入qq号")
    card={}
    card['qq']=qq
    card['wx']=weixin
    card_info.append(card)
    f=open("d:/backup.data",'w')
    f.write(str(card_info))
    f.close()

def read_file_data():
    global card_info
    try:
        f=open("d:/backup.data")
        card_info = eval(f.read())
        f.close()
    except Exception:
        pass
main()