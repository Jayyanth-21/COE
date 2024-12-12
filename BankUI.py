class Bank:
    c = 3
    availb=15000
    def deposit(self):
        x=1
        while(x==1):
            depamt=int(input("Enter ur deposit amount (minimum amt is 100) :"))
            if(depamt<100):
                print("min deposit amount is $100 plz try again... ")
            elif((depamt%100)!=0):
                print("deposit amount should be multiples of 100 notes")
            elif(depamt>50000):
                print("max deposit amount limit is $50000 plz try again... ")
            else:
                self.availb+=depamt
                print("AVAILABLE BALANCE IS : ",self.availb)
                x=2

    def withdraw(self):

        while(self.c>0):
            withamt=int(input("Enter your withdrawl amount: "))
            if withamt<self.availb:
                if(withamt>100):
                    if(withamt<=20000):
                        if(withamt%100==0):
                            if(self.availb-withamt>=500):
                                self.availb-=withamt
                                print("Your money is debited and AVAILABLE BALANCE IS : ",self.availb)
                                obj.denomination(withamt)
                                self.c-=1
                                print("withdrawl transactions left ", self.c)
                                if self.c==0:
                                    print("Ur daily transaction count is completed..plz try after 24hrs")
                            else:
                                print("U must maintain min balance of 500 ,cant debit the money..plz try again")
                        else:
                            print("Enter amt in multiples of 100 notes only...")
                    else:
                        print("Maximum amount per transaction is $20000 only...plz try again")
                else:
                    print("Minimum amount per transaction is $100..plz try again ")
            else:
                print("Ur withdrawl amount is more than available balance cant provide money..plz try again")


    def denomination(self,wdamt):
        if (wdamt//500)>=1:
            _500n=wdamt//500
            wdamt-=_500n*500
            _200n=wdamt//200
            wdamt-=_200n*200
            _100n=wdamt//100
        elif wdamt<500:
            _500n=0
            _200n=wdamt//200
            wdamt -= _200n*200
            _100n=wdamt//100

        print(f"No of $500 notes: {_500n}\n No of $200 notes: {_200n}\n No of 100 notes: {_100n}")



    def pinval(self):

        if(self.c>0):
            pin = int(input("Enter ur pin number : "))
            if  pin==7898:
                obj.viewopt()
            else:
                self.c-=1
                print("wrong pin entered,please try again...")
                print("U r left with",self.c,"chances")
                obj.pinval()

        else:
            print("ur card blocked")



    def viewopt(self):
        print("WELCOME TO SBI BANK")
        ch=0
        while(ch!=4):
            print("choose ur choice from below:")
            print("1.Deposit\n2.Withdraw\n3.Balance Enquiry\n4.Exit")
            ch = int(input("Enter ur choice: "))
            match ch:
                case 1:
                    print("You have chosen Deposit transaction")
                    obj.deposit()
                case 2:
                    print("You have chosen Withdrawl transaction")
                    obj.withdraw()
                case 3:
                    print("You have chosen balance enquiry")
                    print("AVAILABLE BALANCE IS: ",self.availb)
                case 4:
                    print("Application is exitting...")

obj=Bank()
obj.pinval()