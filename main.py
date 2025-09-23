import streamlit as st

st.title("나의 첫 웹 서비스 만들기!")
st.balloons()
name = st.text_input("이름을 입력해주세요. : ")
menu = st.selectbox("가장 많이 쓰는 앱은? : ", ["카카오톡", "네이버", "구글"])
time = st.slider("시간을 선택해주세요. : ", 1, 2, 3)
if st.button("저장"):
    st.write(f"안녕하세요! {name}님 반갑습니다! {menu}를 {time}번 많이 사용합니다.")
    st.snow()
