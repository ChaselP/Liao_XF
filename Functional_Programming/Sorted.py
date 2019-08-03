L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L1=sorted(L,key=lambda x:x[0])
L2=sorted(L,key=lambda x:x[1],reverse=True)

print(L1,L2)


