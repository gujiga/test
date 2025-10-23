"""
Tests for the utils module.
"""
import unittest
from dailyjoke.utils import get_random_joke, get_daily_joke

class TestUtils(unittest.TestCase):
    
    def test_get_random_joke_returns_string(self):
        """测试get_random_joke返回的是字符串类型"""
        joke = get_random_joke()
        self.assertIsInstance(joke, str)
        self.assertTrue(len(joke) > 0)
    
    def test_get_daily_joke_returns_same_for_same_day(self):
        """测试同一天get_daily_joke返回相同的笑话"""
        joke1 = get_daily_joke()
        joke2 = get_daily_joke()
        self.assertEqual(joke1, joke2)
    
    def test_jokes_are_from_predefined_list(self):
        """测试返回的笑话来自预定义列表"""
        # 内置笑话列表（从utils.py中复制）
        expected_jokes = [
            "为什么程序员总是分不清万圣节和圣诞节？因为 Oct 31 = Dec 25。",
            "为什么Python是最好的语言？因为它有蛇的优雅和龙的力量！",
            "一个SQL注入走进酒吧，看到两张桌子，问：'你们都叫什么名字？'",
            "为什么程序员喜欢黑暗模式？因为光明会导致错误。",
            "什么是永远不会错的编程建议？使用更多的分号！（对某些语言而言）"
        ]
        
        # 多次调用以增加覆盖概率
        jokes_set = set()
        for _ in range(20):
            jokes_set.add(get_random_joke())
        
        # 确保所有返回的笑话都在预定义列表中
        for joke in jokes_set:
            self.assertIn(joke, expected_jokes)

if __name__ == '__main__':
    unittest.main()