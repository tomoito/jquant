import requests
import json

def get_tokens():
    ## リフレッシュトークンを取得
    data={"mailaddress":"tomotun1210@gmail.com", "password":"Kojirou266Kojirou266"}
    r_post = requests.post("https://api.jquants.com/v1/token/auth_user", data=json.dumps(data))
    r_post.json()
    
    ## IDトークンを取得
    REFRESH_TOKEN = r_post.json()['refreshToken']
    refresh_result = requests.post(f"https://api.jquants.com/v1/token/auth_refresh?refreshtoken={REFRESH_TOKEN}")
    refresh_result.json()
    
    return refresh_result.json()["idToken"]