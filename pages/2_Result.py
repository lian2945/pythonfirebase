import streamlit as st
st.bar_chart({"data":[1,5,2,6,2,1]})

with st.expander("See explanation"):
    if 'answer' in st.session_state:
        st.write(st.session_state.answer)
        st.image("https://static.streamlit.io/examples/dice.jpg")