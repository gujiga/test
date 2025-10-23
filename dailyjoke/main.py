"""
Main entry point for the daily joke command line tool.
"""
import argparse
from .utils import get_random_joke, get_daily_joke

def main() -> None:
    """
    命令行工具的主入口函数。
    """
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='获取每日笑话或随机笑话')
    parser.add_argument('--type', choices=['daily', 'random'], default='daily',
                        help='笑话类型：daily（每日笑话）或 random（随机笑话）')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 根据参数获取笑话
    if args.type == 'daily':
        joke = get_daily_joke()
        print("📅 今日笑话：")
    else:
        joke = get_random_joke()
        print("🎲 随机笑话：")
    
    # 打印笑话
    print(joke)
    print("\n😂 希望这个笑话能让你的一天更愉快！")

if __name__ == '__main__':
    main()