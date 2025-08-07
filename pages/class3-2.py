import streamlit as st

# 重新整理畫面
if st.button("重新整理"):
    st.markdown(
        '<div style="background-color:#d4edda;color:#155724;padding:10px;border-radius:5px;">準備重新整理...</div>',
        unsafe_allow_html=True,
    )
    import time

    time.sleep(3)
    st.rerun()

# 設定標題
st.title("點餐機")

# 初始化購物籃
if "cart" not in st.session_state:
    st.session_state.cart = []

# 輸入餐點名稱
col1, col2 = st.columns([3, 1])
with col1:
    food = st.text_input("請輸入餐點", "")
with col2:
    if st.button("加入"):
        if food:
            st.session_state.cart.append(food)
            st.rerun()
        else:
            st.warning("請輸入餐點")

# 顯示購物籃內容
st.subheader("購物籃")

if st.session_state.cart:
    for idx, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([4, 1])
        col1.write(f"{item}")
        if col2.button("刪除", key=f"del_{idx}"):
            st.session_state.cart.pop(idx)
            st.rerun()
