"""
Utility functions for the daily joke package.
"""
import requests
import random
from datetime import datetime

# API端点
JOKE_API_URL = "https://official-joke-api.appspot.com/random_joke"

# 缓存每日笑话，避免重复请求
_daily_joke_cache = {}

def get_random_joke() -> str:
    """
    从API获取一个随机笑话。
    
    Returns:
        str: 随机笑话内容（setup + punchline）
    """
    try:
        # 发送请求到笑话API
        response = requests.get(JOKE_API_URL, timeout=5)
        response.raise_for_status()  # 检查请求是否成功
        
        # 解析JSON响应
        joke_data = response.json()
        
        # 组合笑话的setup和punchline部分
        # 示例API返回格式: {"type": "general", "setup": "...", "punchline": "...", "id": 123}
        return f"{joke_data['setup']} {joke_data['punchline']}"
        
    except Exception as e:  # 捕获所有异常
        # 如果API调用失败，使用备用笑话
        fallback_jokes = [
            "为什么程序员总是分不清万圣节和圣诞节？因为 Oct 31 = Dec 25。",
            "为什么Python是最好的语言？因为它有蛇的优雅和龙的力量！",
            "一个SQL注入走进酒吧，看到两张桌子，问：'你们都叫什么名字？'",
            "为什么程序员喜欢黑暗模式？因为光明会导致错误。",
            "什么是永远不会错的编程建议？使用更多的分号！（对某些语言而言）"
        ]
        # 记录错误（实际应用中可以使用日志库）
        print(f"获取笑话API失败: {e}")
        return random.choice(fallback_jokes)

def get_daily_joke() -> str:
    """
    获取每日笑话。
    确保同一天内返回相同的笑话。
    
    Returns:
        str: 每日笑话内容
    """
    # 获取今天的日期字符串作为缓存键
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 检查缓存中是否已有今日笑话
    if today not in _daily_joke_cache:
        # 如果没有，获取新笑话并缓存
        _daily_joke_cache[today] = get_random_joke()
    
    # 返回缓存的今日笑话
    return _daily_joke_cache[today]