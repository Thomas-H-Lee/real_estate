# 1. 카톡 인증 받기
# import requests

# url = 'https://kauth.kakao.com/oauth/token'
# rest_api_key = '98f1390dcc805ab2565521fa12367ced'
# redirect_uri = 'http://182.225.112.168:8501/'
# authorize_code = 'K9n_lFSFN8yhzmcptsWqcD6xbkE_FUrkQzjD3OdT7GFmXeDof5X0X29K4U3zzg0eLWBvfgo9dRoAAAF9pzosfA'

# data = {
#     'grant_type':'authorization_code',
#     'client_id':rest_api_key,
#     'redirect_uri':redirect_uri,
#     'code': authorize_code,
#     }

# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)

# # json 저장
# import json
# with open("kakao_code.json","w") as fp:
#     json.dump(tokens, fp)
    
 
    
# 2. json 읽어오기
import json

with open("kakao_code.json","r") as fp:
    ts = json.load(fp)
print(ts)
print(ts["access_token"])

## 3. 메세지 보내기z
# import os
# import json
# import requests

# def sendToMeMessage(text):
#     with open("kakao_code.json","r") as fp:
#         tokens = json.load(fp)
        
#     access_token = tokens["access_token"]
    
#     header = {"Authorization": 'Bearer ' + access_token}

#     url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소

#     post = {
#         "object_type": "text",
#         "text": text,
#         "link": {
#             "web_url": "https://developers.kakao.com",
#             "mobile_web_url": "https://developers.kakao.com"
#         },
#         "button_title": "바로 확인"
#     }
#     data = {"template_object": json.dumps(post)}
#     return requests.post(url, headers=header, data=data)

# # text = "Hello, This is KaKao Message Test!!("+os.path.basename(__file__).replace(".py", ")")
# text = "Hello, This is KaKao Message Test!!"

# print(sendToMeMessage(text).text)
