'''
v1.03
    新增功能：
    创建游戏窗口
    用到游戏引擎中的功能模块
    官方开发文档
'''
import pygame
_display = pygame.display
class MainGame():
    #游戏主窗口
    window = None
    Screen_height = 500
    Screen_width = 800
    COLOR_BLACK =pygame.Color(0,0,0)
    def __init__(self):
        pass
    def startGame(self):
        '''开始游戏方法'''
        #创建窗口，加载窗口
        _display.init()
        #创建游戏窗口
        MainGame.window=_display.set_mode((MainGame.Screen_height,MainGame.Screen_width))
        #设置一下游戏标题
        _display.set_caption('坦克大战v1.03')
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色
            MainGame.window.fill(MainGame.COLOR_BLACK)
            _display.update()
    def endGame(self):
        '''结束游戏方法'''
        print('谢谢使用')
        #结束python解释器
        exit()

class Tank():
    def __init__(self):
        pass
    def move(self):
        '''移动坦克方法'''
        pass
    def shot(self):
        '''坦克射击方法'''
        pass
    def displayTank(self):
        '''展示坦克'''
        pass
class MyTank(Tank):
    def __init__(self):
        pass
class EnemyTank(Tank):
    def __init__(self):
        pass
class Bullet():
    def __init__(self):
        pass
    def move(self):
        '''移动子弹的方法'''
        pass
    def displayBullet(self):
        '''展示子弹的方法'''
        pass
class Explode():
    def __init__(self):
        pass
    def dispalyExplode(self):
        '''展示爆炸'''
        pass
class Wall():
    def __init__(self):
        pass
    def displayWall(self):
        '''展示墙壁'''
        pass
class Music():
    def __init__(self):
        pass
    def play(self):
        '''开始播放音乐'''
        pass

MainGame().startGame()