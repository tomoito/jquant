import requests
import json
import jquantsapi
from requests import HTTPError


def get_tokens2():
    ## リフレッシュトークンを取得
    data={"mailaddress":"tomotun1210@gmail.com", "password":"Kojirou266Kojirou266"}
    r_post = requests.post("https://api.jquants.com/v1/token/auth_user", data=json.dumps(data))

    #リフレッシュトークン
    return  r_post.json()['refreshToken']

    # cli = jquantsapi.Client(refresh_token=refresh_token)
    # try:
    #     id_token = cli.get_id_token()
    #     if len(id_token) > 0:
    #         print("refresh_tokenは正常です。")
    #     return id_token
    # except HTTPError:
    #     print("refresh_tokenを使用できません。再度値を確認してください。")
