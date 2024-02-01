# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time: 2024/2/1 15:16
@Author: shiqixin.set
@File: bot.py
@Software: PyCharm
@desc: 
"""

import nonebot
from pathlib import Path

nonebot.init()

nonebot.load_plugins("plugins")


nonebot.run()
