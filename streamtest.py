import streamlit as st
st.title("Even or odd finder ")
n1=st.number_input("Enter a number to know if its odd or even",min_value=1,step=1)
if st.button("CHECK"):
    if n1%2==0:
        st.success(f"{n1} is a Even number")
    else:
        st.error(f"{n1} is a Odd number")

