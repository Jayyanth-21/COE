bsal=int(input("Enter ur basic salary: "))
if bsal<=10000:
    hra=(67/100)*bsal
    da=(73/100)*bsal
elif bsal<=20000:
    hra=(69/100)*bsal
    da = (76/100) * bsal
else:
    hra = (73 / 100) * bsal
    da = (89 / 100) * bsal

gs=bsal+hra+da
print("basic salary is : ",bsal)
print("HRA is : ",hra)
print("DA : ",da)
print("gross salary is : ",gs)
