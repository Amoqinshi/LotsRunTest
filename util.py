# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：LotsRunTest
@File ：util.py
@Author ：琴师
@Date ：2023/6/27 12:07 下午
"""

import base64
import json


def Base64Conveter(strs):
    if isinstance(strs, dict):
        text = base64.b64encode((json.dumps(strs)).encode("utf-8"))
        return text.decode('utf-8')

    else:
        text = base64.b64encode(strs).encode("utf-8")
        return text.decode('utf-8')
