#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time ：2022/8/19 10:20
@Auth ：小呆瓜
@File ：main.py
@IDE ：PyCharm
@Description：微信公众号发送消息主文件
"""

from send_message import SendMessage


class Main(object):
    def __init__(self) -> None:
        """
        构造函数
        """
        pass

    def main(self) -> None:
        # 实例SendMessage
        sm = SendMessage()
        # 获取接口返回数据
        json_data = {"name": "小呆瓜", "code": "666666"}
        # 发送消息
        sm.send_message(json_data=json_data)


if __name__ == '__main__':
    main = Main()
    main.main()
