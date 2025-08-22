'''
游戏引擎的安装
1. pip install pygame
2. pycharm安装 file ->setting->project->project interpreter->右侧+install->搜索框输入pygame->下方installpackage

明白需求：（基于面向对象的分析）
1.有那些类 2.不同的类所具备的一些功能
    1.主逻辑类
        开始游戏
        结束游戏
    2.坦克类（敌方坦克 己方坦克）
        移动
        射击
    3.子弹
        移动
    4.爆炸效果
        展示爆炸效果
    5.墙壁
        属性：是否可以通过
    6.音效类
        播放音乐
3. 坦克大战项目框架的搭建
    涉及到的类，用代码简单的实现
'''
import pygame
class MainGame():
    def __init__(self):
        pass
    def startGame(self):
        pass
    def endGame(self):
        pass
