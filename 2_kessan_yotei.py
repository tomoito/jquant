from get_tokens import get_tokens
import requests
import pandas as pd


id_token = get_tokens()
print(id_token)

headers = {'Authorization': 'Bearer {}'.format(id_token)}
r = requests.get("https://api.jquants.com/v1/fins/announcement", headers=headers)
r.json()

print(r.json())
