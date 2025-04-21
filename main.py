import streamlit as st

# I can add a Excel sheet......
# dataset = pd.read_excel("Practice1.xlsx")
# st.dataframe(dataset)

# called a Graphic inter

# I can add a Excel sheet......
# dataset = pd.read_excel("Practice1.xlsx")
# st.dataframe(dataset)

# called a Graphic inter userface..
name = st.text_input("Enter your name:")
fname = st.text_input("Enter your Father name:")
address = st.text_area("enter your text:")
#selectbox = used for a Dropdown list B.R
classdata = st.selectbox("enter your class :", (1,2,3,4,5,6))

button = st.button("SUBMIT")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    adr : {address}
    class : {classdata}""")

# Most B.R {} curly bracket valid karva f""" no use thase..
