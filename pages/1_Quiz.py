import streamlit as st
st.session_state.score=0
st.session_state.answer="NULL"
st.header("1. 왕이 넘어지면?")
st.divider()
st.session_state.answer=st.text_area(label="**답**")
if st.button("제출"):
    st.divider()
    st.header("결과")
    if st.session_state.answer == "킹콩":
        st.session_state.score+=50
        st.markdown("정답입니다.")
    else:
        st.markdown("오답입니다.")
    st.divider()
    answer2=st.radio("내 이름은?", ["김동하", "김도운", "김어눌", "김동욱", "김으나"])
    if answer2=="김동욱":
        st.session_state.score+=50
    st.write(st.session_state.score)