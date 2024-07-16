import streamlit as st
st.header("1. 왕이 넘어지면?")
st.divider()
st.session_state.answer=st.text_area(label="**답**")
st.divider()
answer2=st.radio("2. 내 이름은?", ["김동하", "김도운", "김어눌", "김동욱", "김으나"])
if st.button("제출하기"):
    st.session_state.score=0
    if answer2=="김동욱":
        st.session_state.score+=50
    if st.session_state.answer == "킹콩":
        st.session_state.score+=50
    st.switch_page("pages/2_Result.py")