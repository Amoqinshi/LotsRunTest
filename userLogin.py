# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：LotsRunTest
@File ：userLogin.py
@Author ：琴师
@Date ：2023/6/16 10:12 上午
"""

import requests
import json


def get_contents():
    with open("loginData.json", "r+") as f:
        data_dict = json.loads(f.read())
        url = data_dict.get("env").get("fat")
        method = data_dict.get("method")
        headers = data_dict.get("headers")
        payload = data_dict.get("data").get("fat")
        org_id = data_dict.get("data_org_id")
        org_code = data_dict.get("data_org_code")
        qy_id = data_dict.get("qy_id")

    content = url, method, headers, payload, org_id, org_code, qy_id
    return content


def login():
    res = requests.request(
        method=get_contents()[1],
        url=get_contents()[0],
        headers=get_contents()[2],
        data=get_contents()[3])
    user_token = json.loads(res.text)
    return user_token.get("access_token")


# def blind():
#     params = {
#         "org_id": get_contents()[4],
#         "access_token": login()[0],
#         "refresh_token": login()[1]}
#     url = "http://sso.my-fat.gaoding.com/api/token/org-bind"
#     headers = {
#         "Content-Type": "application/json",
#         'x-product-type': 'FREE',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/114.0.0.0 Safari/537.36',
#         'authority': 'sso.my-fat.gaoding.com',
#
#     }
#     response = requests.request("POST",
#                                 url,
#                                 headers=headers,
#                                 data=json.dumps(params),
#                                 )
#     print(response.text)


def org_select():
    params = {
        "org_id": get_contents()[4],
        "access_token": login(),
        "grant_type": "org",
        "client_id": get_contents()[3].get("client_id"),
        "device_id": get_contents()[3].get("device_id")

    }
    url = "http://sso.my-fat.gaoding.com/api/oauth/token/v2/org-select"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        'x-product-type': 'FREE',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/114.0.0.0 Safari/537.36',
        'authority': 'sso.my-fat.gaoding.com',

    }
    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=params
                                )
    user_token = json.loads(response.text)
    return user_token.get("access_token")


if __name__ == "__main__":
    pass
