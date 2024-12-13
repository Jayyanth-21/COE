import streamlit as st

st.title('WELCOME TO COE BANK')


class Bank:
    def __init__(self):
        if 'availb' not in st.session_state:
            st.session_state.availb = 15000
        if 'c' not in st.session_state:
            st.session_state.c = 4

    def pinval(self):
        while st.session_state.c > 0:
            pin = st.number_input("Enter the pin number", value=None, key="pin_input")

            if pin == 7898:
                self.viewopt()
                break
            else:
                st.session_state.c -= 1
                st.error("Wrong pin entered, please try again...")
                st.error(f"You are left with {st.session_state.c} chances")

        if st.session_state.c == 0:
            st.error("Your card is blocked")

    def deposit(self):
        x = 1
        while x == 1:
            depamt = st.number_input("Enter your deposit amount (minimum amount is 100):", min_value=100, step=1,
                                     key="deposit_input")
            if st.button("DEPOSIT"):
                if depamt < 100:
                    st.error("Minimum deposit amount is $100. Please try again...")
                elif depamt % 100 != 0:
                    st.error("Deposit amount should be in multiples of 100 notes.")
                elif depamt > 50000:
                    st.error("Maximum deposit amount is $50000. Please try again...")
                else:
                    st.session_state.availb += depamt
                    st.success(f"Amount successfully deposited into your bank account.")
                    st.success(f"AVAILABLE BALANCE IS: {st.session_state.availb}")\0

                    x = 2

    def withdraw(self):
        x = 1
        while x == 1:
            withamt = st.number_input("Enter your withdrawal amount:", min_value=100, step=1,
                                      key="withdraw_input")
            if st.button("WITHDRAW"):
                if withamt <= st.session_state.availb:
                    if withamt >= 100:
                        if withamt <= 20000:
                            if withamt % 100 == 0:
                                if st.session_state.availb - withamt >= 500:
                                    st.session_state.availb -= withamt
                                    st.success(
                                        f"Your money is debited. AVAILABLE BALANCE IS: {st.session_state.availb}")
                                    st.session_state.c -= 1
                                    if st.session_state.c == 0:
                                        st.error("Your daily transaction count is completed, Please try after 24hrs.")
                                        x = 2
                                else:
                                    st.error(
                                        "You must maintain a minimum balance of $500, Cannot debit the money...Please try again.")
                            else:
                                st.error("Enter amount in multiples of 100 notes only.")
                        else:
                            st.error("Maximum amount per transaction is $20000 only. Please try again.")
                    else:
                        st.error("Minimum amount per transaction is $100. Please try again.")
                else:
                    st.error(
                        "Your withdrawal amount is more than the available balance, Cannot provide money...Please try again.")

    def viewopt(self):
        while True:
            ch = st.radio("Choose a transaction from below:",
                          options=["1.DEPOSIT", "2.WITHDRAW", "3.BALANCE ENQUIRY", "4.EXIT"],
                          key="menu_choice")

            if ch == "1.DEPOSIT":
                st.success("You have chosen Deposit transaction")
                self.deposit()
            elif ch == "2.WITHDRAW":
                st.success("You have chosen Withdrawal transaction")
                self.withdraw()
            elif ch == "3.BALANCE ENQUIRY":
                st.success("You have chosen balance enquiry")
                st.success(f"AVAILABLE BALANCE IS: {st.session_state.availb}")
            elif ch == "4.EXIT":
                st.success("Application is exiting...")
                st.success("THANK YOU FOR VISITING THE BANK..")
                break


obj = Bank()
obj.pinval()
