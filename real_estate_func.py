import time
import schedule
import os
import json
import requests
import logging
import datetime

# 액세스 토큰 갱신
def refreshToken(refresh_token) :
    REST_API_KEY = "98f1390dcc805ab2565521fa12367ced"
    REDIRECT_URI = "http://182.225.112.168:8501/"

    data = {
        "grant_type": "refresh_token", 
        "client_id": REST_API_KEY,
        "refresh_token": refresh_token # 여기가 위에서 얻은 refresh_token 값
    }
    resp = requests.post(REDIRECT_URI, data=data)
    print(resp)
    new_token = resp.json()

    # kakao_code.json 파일 저장
    with open("kakao_code.json", "w") as fp:
        json.dump(new_token, fp)

#특정 함수 정의
def sendToMeMessage(flg):
    
    content, count = get_realestate_items()

    print(count)
    with open("kakao_code.json","r") as fp:
        tokens = json.load(fp)
    
    access_token = tokens["access_token"]
    
    # access token 유효성 검사 후 false일경우 갱신
    if flg == True:
        pass
    else:
        access_token = refreshToken(tokens["refresh_token"])
        
    
    header = {"Authorization": 'Bearer ' + access_token}

    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소

    for i in range(0, count):
        text = content[i]
        post = {  
            "object_type": "text",
            "text": text,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
            "button_title": "바로 확인"
        }
        data = {"template_object": json.dumps(post)}
        requests.post(url, headers=header, data=data)
        
    print("Message Sent complete")
    flg = False  # 액세스토큰 유효

    return tokens, flg

def get_realestate_items():
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
    content = list(range(0,100)) #총 100개 부동산 물건 적재 리스트 생성
    for item in result:

        dt_now = datetime.datetime.now()
        item1_content = str('\n갱신날짜 : '+str(dt_now.strftime('%Y-%m-%d %H:%M:%S')))
        item2_content = str('\n[물건 ' + str(count+1) + ']')
        item3_content = str('\n타입 : ' + str(item['atclNm'] + '_'+ str(item['rletTpNm'])))
        item4_content = str('\n거래유형 :' + str(item['tradTpNm']))
        item5_content = str('\n매가 : '+ str(item['hanPrc']))
        item6_content = str('\n토지면적 : ' + str(round(item['spc1']/3.3, 0)) +'평')        
        item7_content = str('\n평단가 : ' + str(round(item['prc']*10/item['spc1']/3.3,0)) + '만원')        
        item8_content = str('\n')        
        
        content[count] = item1_content + item2_content + item3_content + item4_content + item5_content + item6_content + item7_content + item8_content 

        count = count+1
        
    final_content = ''
    
    for i in range(0, count): 
        final_content = content[i] + final_content         
        
    
    print(content)
    return content, count
    

flg = True

tokens = sendToMeMessage(flg)
 
#chedule.every(150).minutes.do(refreshToken(tokens["refresh_token"])) #150분마다 리프레쉬 토큰으로 액세스 토큰 갱신(6시간 만료)
#schedule.every().monday.at("00:10").do(printhello) #월요일 00:10분에 실행
schedule.every().day.at("08:00").do(sendToMeMessage) #매일 8시에 
 
#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(1)


