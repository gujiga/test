"""
Tests for the utils module.
"""
import unittest
from unittest.mock import patch, MagicMock
from dailyjoke.utils import get_random_joke, get_daily_joke, _daily_joke_cache

class TestUtils(unittest.TestCase):
    
    def test_get_random_joke_returns_string(self):
        """测试get_random_joke返回的是字符串类型"""
        joke = get_random_joke()
        self.assertIsInstance(joke, str)
        self.assertTrue(len(joke) > 0)
    
    def test_get_daily_joke_returns_same_for_same_day(self):
        """测试同一天get_daily_joke返回相同的笑话"""
        # 清除缓存以确保测试的独立性
        _daily_joke_cache.clear()
        
        joke1 = get_daily_joke()
        joke2 = get_daily_joke()
        self.assertEqual(joke1, joke2)
    
    @patch('dailyjoke.utils.requests.get')
    def test_api_integration(self, mock_get):
        """测试API调用逻辑"""
        # 模拟API响应
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "type": "general",
            "setup": "为什么咖啡报警？",
            "punchline": "因为它被抢劫了。",
            "id": 431
        }
        mock_get.return_value = mock_response
        
        # 调用函数
        joke = get_random_joke()
        
        # 验证结果
        self.assertEqual(joke, "为什么咖啡报警？ 因为它被抢劫了。")
        # 验证API被正确调用
        mock_get.assert_called_once_with("https://official-joke-api.appspot.com/random_joke", timeout=5)
    
    @patch('dailyjoke.utils.requests.get')
    def test_fallback_mechanism(self, mock_get):
        """测试API失败时的回退机制"""
        # 模拟请求异常
        mock_get.side_effect = Exception("网络错误")
        
        # 调用函数，应该返回备用笑话
        joke = get_random_joke()
        
        # 验证返回的是字符串
        self.assertIsInstance(joke, str)
        self.assertTrue(len(joke) > 0)
    
    def test_daily_joke_cache(self):
        """测试每日笑话的缓存机制"""
        # 清除缓存
        _daily_joke_cache.clear()
        
        # 第一次调用应该触发缓存更新
        first_joke = get_daily_joke()
        self.assertEqual(len(_daily_joke_cache), 1)
        
        # 第二次调用应该使用缓存
        second_joke = get_daily_joke()
        self.assertEqual(first_joke, second_joke)

if __name__ == '__main__':
    unittest.main()