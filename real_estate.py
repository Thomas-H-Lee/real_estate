import requests
import json
import logging
import time
import streamlit as st
import datetime

URL = "https://m.land.naver.com/cluster/ajax/articleList"
param = {
    'view': 'atcl',
    'cortarNo' : '4111514100' ,
    'rletTpCd': 'GM:TJ',
    'tradTpCd' : 'A1',
    'z': '16',
    'lat' : '37.2686392',
    'lon' : '127.0326146',
    'btm' : '37.261057',
    'lft' : '127.0217892',
    'top' : '37.2762206',
    'rgt' : '127.04344',
    'pCortarNo': '16_4111514100'       
} 

header = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
    'Connection': 'keep-alive',
    'Host': 'm.land.naver.com',
    'Referer': 'https://m.land.naver.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

logging.basicConfig(level=logging.INFO)
page = 0

st.markdown('네이버 부동산 크롤링')
st.text('인계동 상가 빌딩 매물 리스트')

if st.button('Let\'s Buy it!'):
    page += 1
    param['page'] = page
    time.sleep(2) # 봇 감지 회피용 waiting
    resp = requests.get(URL, params=param, headers=header)
    
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        
    data = json.loads(resp.text)
    print("data=".format(data))

    result = data['body'] # 수신한 데이터 중 'body'만 추출
    
    if result is None:
        logging.error('no result')
    
    count = 0
    for item in result:
        count = count+1

        #logging.info('타입: [%s_%s] ' % (item['atclNm'], item['rletTpNm']))
        #logging.info('거래유형: [%s] ' % (item['tradTpNm']))
        #logging.info('매가(만원): [%s] ' % (round(item['prc'],0)))
        #logging.info('평단가: [%s] ' % (item['prc']/item['spc1']))
        

        dt_now = datetime.datetime.now()
        st.text('갱신날짜 : {}'.format(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
        st.markdown('* * *')
        st.text('물건 {}'.format(count))
        st.text('타입: [{}_{}] '.format(item['atclNm'], item['rletTpNm']))
        st.text('거래유형: [{}] '.format(item['tradTpNm']))
        st.text('매가: [{}만원, {}] '.format(round(item['prc'],0), item['hanPrc']))
        st.text('토지면적: [{}평] '.format(item['spc1']))        
        st.text('평단가: [{}] '.format(round(item['prc']/item['spc1'],0)))        


