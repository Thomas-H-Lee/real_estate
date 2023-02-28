# 셀린 홈페이지 스크래핑
import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText


while True:
    URL = 'https://www.celine.com/ko-kr/celine-%EC%97%AC%EC%84%B1/%ED%95%B8%EB%93%9C%EB%B0%B1/%ED%8A%B8%EB%A6%AC%EC%98%A4%ED%8E%98-%EC%BA%94%EB%B2%84%EC%8A%A4/%EB%AF%B8%EB%8B%88-%EB%B2%A0%EC%82%AC%EC%B2%B4---%ED%8A%B8%EB%A6%AC%EC%98%A4%ED%8E%98-%EC%BA%94%EB%B2%84%EC%8A%A4-and-%EC%B9%B4%ED%94%84%EC%8A%A4%ED%82%A8-196702BZJ.04LU.html'
    html = requests.get(URL).text

    soup = BeautifulSoup(html, 'html.parser')

    stock_div  = soup.find("p", attrs={"data-test": "product-overview-availability"})
                           
    stock_result = stock_div.text
    
    if stock_result != '알림 받기':
        # 세션 생성
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # TLS 보안 시작
        s.starttls()
        # 로그인 인증
        s.login('abovefirst@gmail.com', 'snhwrstvftqdmdiz')
        # 보낼 메시지 설정
        msg = MIMEText('재입고 된 걸로 분석됨.')
        msg['Subject'] = '!!! 셀린느 재입고 알람 !!!'
        # 메일 보내기
        s.sendmail("abovefirst@gmail.com", "abovefirst@gmail.com", msg.as_string())
        # 세션 종료
        s.quit()

    time.sleep(120) # 120초 간격으로 크롤링






