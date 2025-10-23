"""
Utility functions for the daily joke package.
"""
import requests
import random
from datetime import datetime

def get_random_joke() -> str:
    """
    获取一个随机笑话。
    
    Returns:
        str: 随机笑话内容
    """
    # 内置一些示例笑话
    jokes = [
        "为什么程序员总是分不清万圣节和圣诞节？因为 Oct 31 = Dec 25。",
        "为什么Python是最好的语言？因为它有蛇的优雅和龙的力量！",
        "一个SQL注入走进酒吧，看到两张桌子，问：'你们都叫什么名字？'",
        "为什么程序员喜欢黑暗模式？因为光明会导致错误。",
        "什么是永远不会错的编程建议？使用更多的分号！（对某些语言而言）"
    ]
    
    return random.choice(jokes)

def get_daily_joke() -> str:
    """
    获取每日笑话。
    根据当前日期选择固定的笑话，确保同一天内返回相同的笑话。
    
    Returns:
        str: 每日笑话内容
    """
    # 使用当前日期作为种子
    today = datetime.now().strftime('%Y-%m-%d')
    seed = sum(ord(char) for char in today)
    
    # 设置随机种子以确保同一天返回相同的笑话
    random.seed(seed)
    
    return get_random_joke()