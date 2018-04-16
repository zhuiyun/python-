def seach(a):
    if(str(a).isalpha()):
        a=str(a).lower()
        b=0
        for i in a:
            if(a.count(i)>b):
                c=i;
                b=a.count(i)
            elif(a.count(i)==b):
               if(c>i):
                   c=i
        return c

print(seach("ab"))
