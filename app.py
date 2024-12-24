import streamlit as st

# タイトル
st.title("Streamlit Community Cloud Test App")

# テキスト入力
name = st.text_input("What's your name?")

# ボタンと結果
if st.button("Submit"):
    st.write(f"Hello, {name}!")
else:
    st.write("Enter your name and click Submit.")
