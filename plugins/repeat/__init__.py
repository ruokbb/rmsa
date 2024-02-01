# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2024/2/1 15:17
@Author: shiqixin.set
@File: __init__.py.py
@Software: PyCharm
@desc: 
"""

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.adapters.onebot.v12 import Message, MessageSegment
from nonebot.params import CommandArg

repeat = on_command("repeat", rule=to_me(), aliases={"复读"}, priority=10, block=True)

@repeat.handle()
async def handler(args: Message = CommandArg()):
    """
    时间处理
    :return:
    """
    if text := args.extract_plain_text():
        await repeat.finish(text)
    else:
        await repeat.finish("复读nm")

