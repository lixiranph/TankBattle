'''
v1.10
    优化功能：
        按↑松开再立刻按↓就只动一下就停
        用 Clock 控帧；删掉 time.sleep(0.02)
'''
import pygame
import time
_display = pygame.display
version='v1.09'
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_BLACK = pygame.Color(0, 0, 0)
#游戏主窗口
class MainGame():
    window = None
    Screen_height = 500
    Screen_width = 800
    #创建我方坦克
    TANK_P1=None
    def __init__(self):
        pass

    def startGame(self):
        '''开始游戏方法'''
        #创建窗口，加载窗口
        _display.init()
        #创建游戏窗口
        MainGame.window=_display.set_mode((MainGame.Screen_width,MainGame.Screen_height))
        #创建我方坦克
        MainGame.TANK_P1=Tank(400,MainGame.Screen_height-200)
        #设置一下游戏标题
        _display.set_caption(f'坦克大战{version}')
        clock = pygame.time.Clock()# ← 新增：帧率控制
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvents()
            #将绘制文字得到的画布，粘贴到窗口中
            self.handleContinuousMove()  # ← 新增：每帧处理长按连续移动

            MainGame.window.blit(self.getTextSurface(f'剩余敌方坦克5辆'),(5,5))
            #将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            #根据坦克开关状态调用坦克的移动方法
            # if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
            #     MainGame.TANK_P1.move()

            #窗口的刷新
            _display.update()
            clock.tick(60)  # ← 用 tick 控帧，代替 time.sleep

    def getTextSurface(self,text):
        '''左上角文字绘制的功能'''
        #初始化字体模块
        pygame.font.init()
        #选中一个合适的字体
        font = pygame.font.SysFont('仿宋gb2312', 18)
        # 使用对应的字符完成相关内容的绘制
        textSurface=font.render(text,True,COLOR_RED)
        return textSurface

    def handleContinuousMove(self):
        """连续移动：每帧读取当前键盘状态"""
        keys = pygame.key.get_pressed()
        p1 = MainGame.TANK_P1
        if not p1:
            return

        # 若当前朝向对应的键仍被按着，就保留当前朝向；否则在优先序里选一个正在按的方向
        pressed_any = False
        if p1.direction == 'L' and keys[pygame.K_LEFT]:
            pressed_any = True
        elif p1.direction == 'R' and keys[pygame.K_RIGHT]:
            pressed_any = True
        elif p1.direction == 'U' and keys[pygame.K_UP]:
            pressed_any = True
        elif p1.direction == 'D' and keys[pygame.K_DOWN]:
            pressed_any = True
        else:
            if keys[pygame.K_LEFT]:
                p1.direction = 'L';
                pressed_any = True
            elif keys[pygame.K_RIGHT]:
                p1.direction = 'R';
                pressed_any = True
            elif keys[pygame.K_UP]:
                p1.direction = 'U';
                pressed_any = True
            elif keys[pygame.K_DOWN]:
                p1.direction = 'D';
                pressed_any = True

        if pressed_any:
            p1.move()
        # 如果四个方向都没按，什么都不做 => 自然“停下来”

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
                    MainGame.TANK_P1.direction = 'L'
                elif event.key == pygame.K_RIGHT:
                    MainGame.TANK_P1.direction = 'R'
                elif event.key == pygame.K_UP:
                    MainGame.TANK_P1.direction = 'U'
                elif event.key == pygame.K_DOWN:
                    MainGame.TANK_P1.direction = 'D'
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
            # if event.type == pygame.KEYUP:
            #     #修改坦克的移动状态
            #     #松开的如果是方向键，才更改移动开关状态
            #     if (event.key == pygame.K_LEFT
            #             or event.key == pygame.K_RIGHT
            #             or event.key == pygame.K_UP
            #             or event.key == pygame.K_DOWN):
            #         MainGame.TANK_P1.stop=True
    def endGame(self):
        '''结束游戏方法'''
        print('谢谢使用')
        #结束python解释器
        exit()
class Tank():
    def __init__(self,left,top):
        self.images = {
            'U': pygame.image.load(r'Mytank/p1tankU.png').convert_alpha(),
            'D': pygame.image.load(r'Mytank/p1tankD.png').convert_alpha(),
            'L': pygame.image.load(r'Mytank/p1tankL.png').convert_alpha(),
            'R': pygame.image.load(r'Mytank/p1tankR.png').convert_alpha()
        }
        self.direction='U'
        self.image=self.images[self.direction]
        #坦克所在的区域 Rect类型
        self.rect=self.image.get_rect()
        #指定坦克初始化位置 分别距X，Y轴的位置
        self.rect.left=left
        self.rect.top=top
        #新增速度属性
        self.speed=5
        #新增属性：坦克的移动开关
        self.stop=True
    def move(self):
        '''移动坦克方法'''
        if self.direction=='L':
             self.rect.left = max(0, self.rect.left - self.speed)
        elif self.direction=='R':
             self.rect.left = min(MainGame.Screen_width - self.rect.width,
                                  self.rect.left + self.speed)
        elif self.direction=='U':
             self.rect.top = max(0, self.rect.top - self.speed)
        elif self.direction=='D':
            self.rect.top = min(MainGame.Screen_height - self.rect.height,
                                 self.rect.top + self.speed)
    def shot(self):
        '''坦克射击方法'''
        pass
    def displayTank(self):
        '''展示坦克（将坦克绘制到窗口中blit()）'''
        #重新设置坦克的图片
        self.image = self.images[self.direction]
        #将坦克加入到窗口中
        MainGame.window.blit(self.image, self.rect)

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
