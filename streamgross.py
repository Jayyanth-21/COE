import streamlit as st
st.title("Gross salary calc")
bsal=st.number_input("Enter your basic salary: ",min_value=0,step=1)

hra = 0
da = 0
if st.button("Calculate the Gross salary"):

    if bsal<10000:
        hra = (67 / 100) * bsal
        da = (73 / 100) * bsal
    elif bsal <= 20000:
        hra = (69 / 100) * bsal
        da = (76 / 100) * bsal
    else:
        hra = (73 / 100) * bsal
        da = (89 / 100) * bsal

gs=hra+da+bsal
st.success(f"Your gross salary is : {gs}")
