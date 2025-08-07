import random as r
import streamlit as st


u = st.number_input("請猜一個1到100的數字", step=1, min_value=1, max_value=100)

if r == "":
    r = r.randint(1, 100)
if st.button("加入", key="123456abcd"):
    if u == r:
        c = "猜中了"

        r = ""

    elif u < r:
        c = "再大一點"

    elif u > r:
        c = "再小一點"
    st.write(c)
    st.write(r)
st.rerun()
