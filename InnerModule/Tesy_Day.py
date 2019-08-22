def year(y):
    if(y%4==0 and y%100!=0) or(y%400==0):
        return 366
    else:
        return 365

def yearmon(y,m):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    elif m==4 or m==6 or m==9 or m==11:
        return 30
    elif m==2 and year(y)==366:
        return 29
    elif m==2 and year(y)==365:
        return 28
    else:
        print('error input month')

def day(y,m,d):
    sum=0
    i=1900
    j=1
    while i<y:
        sum+=year(i)
        i+=1
    while j<m:
        sum+=yearmon(y,j)
        j+=1
    sum+=d
    f=sum%7
    return f

print(day(2019,8,18))