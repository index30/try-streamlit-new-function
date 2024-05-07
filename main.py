import streamlit as st

button1 = st.button("シンプルなボタン")
def approve_button():
    st.session_state["ok_button1"] = True

if button1:
    st.markdown("本当に良い？")
    st.button("OK", on_click=approve_button)

if st.session_state.get("ok_button1", False):
    st.success("承認されました")