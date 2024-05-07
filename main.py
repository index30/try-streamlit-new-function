import streamlit as st

button1 = st.button("シンプルなボタン")
def approve_button1():
    st.session_state["ok_button1"] = True

def approve_button2():
    st.session_state["ok_button2"] = True
    
@st.experimental_dialog("承認確認")
def approve_button3():
    st.write("本当に良い？")
    if st.button("OKですって"):
        st.session_state["ok_button3"] = True
        st.rerun()

if button1:
    st.markdown("本当に良い？")
    st.button("OK", on_click=approve_button1, key="1")

if st.session_state.get("ok_button1", False):
    st.success("承認されました1")

with st.popover("ポップオーバーのボタン"):
    st.markdown("本当に良い？")
    st.button("OKだよ", on_click=approve_button2, key="2")
if st.session_state.get("ok_button2", False):
    st.success("承認されました2")

if "ok_button3" not in st.session_state:
    if st.button("承認"):
        approve_button3()

if st.session_state.get("ok_button3", False):
    st.success("承認されました3")