# -*- coding: utf-8 -*-

import requests

server = input()
port = int(input())
a = int(input())
b = int(input())

server_url = f'{server}:{port}'

params = {
    'a': a,
    'b': b
}
print(server_url, params)
resp = requests.get(server_url, params=params)
response_json = resp.json()
result = response_json['result']
result = sorted(result)
check = response_json['check']
print(result)
print(check)
