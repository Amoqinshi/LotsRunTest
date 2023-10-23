# !/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：LotsRunTest
@File ：runTest.py
@Author ：琴师
@Date ：2023/3/25 12:39 下午
"""

from threading import Thread
from Generate import test_api, getData
import time


def run(exec_times):
    """
:param exec_times: 测试次数
:return: 执行入口
"""
    threads = []
    time1 = time.process_time()
    for i in range(exec_times):
        thread = Thread(target=test_api(**getData()))
        thread.setDaemon(True)
        threads.append(thread)
    for t in threads:
        t.start()
        t.join()
    time2 = time.process_time()
    print("===============测试结果===================")
    print("批量执行任务数:", exec_times)
    print("总耗时(秒):", time2 - time1)
    print("每次请求耗时(秒):", (time2 - time1) / exec_times)


if __name__ == "__main__":
    run(3)
    print("执行结束")
