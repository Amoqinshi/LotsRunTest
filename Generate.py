# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：LotsRunTest
@File ：Image.py
@Author ：琴师
@Date ：2023/3/25 12:39 下午
"""

from userLogin import org_select, get_contents
from util import Base64Conveter
import json
import re
import requests


def getData():
    """
获取Json数据
"""
    with open("requestData.json", "r+", encoding="utf-8") as fp:
        strdata = json.load(fp)
        # text = re.sub(r"\n|\t|\r｜\r\n|\n\r|\x08|\\", "", strdata)
        return strdata


#
def test_api(**kwargs):
    """
:param kwargs: 数据json
:return 接口请求
"""
    # userinfo = get_contents()[-1]
    # org_id = get_contents()[4]
    # org_code = get_contents()[5]
    # jsonData = {"user_id": userinfo}
    # jsonData1 = {"org_id": org_id, "org_code": org_code}
    request_method = kwargs.get("method")
    request_url = kwargs.get("env").get(
        "fat") + kwargs.get("image").get("path")
    request_headers = kwargs.get("headers")
    request_headers["authorization"] = "Bearer " + org_select()
    # request_headers["user-info"] = Base64Conveter((str(jsonData)).replace("'", "\""))
    # request_headers["org-info"] = Base64Conveter((str(jsonData1)).replace("'", "\""))
    request_data = kwargs.get("image").get("data")
    r = requests.request(
        request_method,
        request_url,
        headers=request_headers,
        data=json.dumps(request_data),
        # verify=False
    )
    print(str(r.text))


if __name__ == "__main__":
    # pass
    print(test_api(**getData()))
