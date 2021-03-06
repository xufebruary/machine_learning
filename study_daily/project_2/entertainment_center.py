#-*- coding: utf-8 -*-

"""
该模块主要为项目运行模块，主要负责接收用户输入，调用
其他模块方法以及使用其他模块类，并最终生成html静态文件
"""

from media import Movie
from fresh_tomatoes import open_movies_page
from scantter import get_douban,get_paofan

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def user_input():
    """
    This function for receive user input love movie name, spite with "，", end with enter.
    
    Returns:
        Return user input string.
    """
    keys = raw_input('输入喜爱的电影，并使用中文逗号分割：\n').split('，')
    return keys

if __name__ == '__main__':
    keys = user_input()
    movies = []
    for key in keys:
        movies += get_paofan(key)
    for movie in movies:
        print movie
    open_movies_page(movies)
