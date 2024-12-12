psc=int(input("Enter project score: "))
isc=int(input("Enter internal score: "))
esc=int(input("Enter external score: "))
if(psc>=50 and isc>=50 and esc>=50):
    totsc=(0.7*psc)+(0.1*isc)+(0.2*esc)
    print("Total score is: ",totsc)
    if(totsc>90):
        print("A")
    elif(totsc>=80):
        print("B")
    elif(totsc>=50):
        print("C")
else:
    if(psc<50):
        print("Student is failed in project")
    if(isc<50):
        print("Student is failed in internals")
    if(esc<50):
        print("Student is failed in externals")
