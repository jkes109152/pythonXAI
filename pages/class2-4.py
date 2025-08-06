import streamlit as st

st.title("數字金字塔")
st.markdown(" 請輸入一個整數(1到9)")
number = st.number_input("數字", step=1, min_value=1, max_value=9)
st.markdown(" 數字金字塔:")
for i in range(1, number + 1):
    x = str(i)
    st.write(x * i)
