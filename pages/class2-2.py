import streamlit as st

# st.number_input()可以讓使用者輸入數字，設定step=1可以讓使用者只能輸入整數
# min_value=0可以設定座小值為0，max_value=100可以設定最大值為100
number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100)
# st.markdown()可以讓網頁使用Markdown語法來顯示文字
st.markdown(f"你輸入的數字是：{number}")
x = st.number_input("請輸入成績", step=1, min_value=0, max_value=100)
y = "?"

if x < 60:
    y = "F"
elif 70 > x >= 60:
    y = "D"
elif 80 > x >= 70:
    y = "C"
elif 90 > x >= 80:
    y = "B"
else:
    y = "A"
st.markdown(f"你的等級是：{y}")
