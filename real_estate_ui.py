import streamlit as st
import datetime

st.markdown('네이버 부동산 크롤링')
st.text('인계동 상가 빌딩 매물 리스트')

dt_now = datetime.datetime.now()
st.text('갱신 : {}'.format(dt_now.strftime('%Y-%m-%d %H:%M:%S')))

st.text('')