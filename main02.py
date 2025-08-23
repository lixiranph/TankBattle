'''
v1.04
    新增功能：
    事件处理：
        点击关闭按钮，退出程序事件
        方向控制，子弹发射
'''
import pygame
_display = pygame.display
version='v1.04'
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
        _display.set_caption(f'坦克大战{version}')
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色
            MainGame.window.fill(MainGame.COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvents()
            _display.update()
    def getEvents(self):
        '''获取程序期间所有的事件（鼠标事件，键盘事件）'''
        #1.获取所有事件
        eventlist = pygame.event.get()
        #2.对事件进行判断处理（1.点击关闭按钮 2.按下键盘上的某个按键）
        for event in eventlist:
            #判断event.type的类型是否为退出,如果是退出直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()
            #判断事件类型是否为按键按下，如果是，继续判断按键是哪一个按键，来进行对应的处理
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print('坦克向左掉头，移动')
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右掉头，移动')
                elif event.key == pygame.K_UP:
                    print('坦克向上掉头，移动')
                elif event.key == pygame.K_DOWN:
                    print('坦克向下掉头，移动')
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
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

if __name__ == '__main__':
    MainGame().startGame()