'''
v1.09
    优化功能：
        优化坦克的移动方法
        按住键盘方向键持续移动
'''
import pygame
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
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvents()
            #将绘制文字得到的画布，粘贴到窗口中
            MainGame.window.blit(self.getTextSurface(f'剩余敌方坦克5辆'),(5,5))
            #将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            #窗口的刷新
            _display.update()

    def getTextSurface(self,text):
        '''左上角文字绘制的功能'''
        #初始化字体模块
        pygame.font.init()
        #选中一个合适的字体
        font = pygame.font.SysFont('仿宋gb2312', 18)
        # 使用对应的字符完成相关内容的绘制
        textSurface=font.render(text,True,COLOR_RED)
        return textSurface

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
                    #修改坦克方向
                    MainGame.TANK_P1.direction='L'
                    #完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_RIGHT:
                    print('坦克向右掉头，移动')
                    #修改坦克方向
                    MainGame.TANK_P1.direction='R'
                    #完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_UP:
                    print('坦克向上掉头，移动')
                    #修改坦克方向
                    MainGame.TANK_P1.direction='U'
                    #完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_DOWN:
                    print('坦克向下掉头，移动')
                    #修改坦克方向
                    MainGame.TANK_P1.direction='D'
                    #完成移动操作（调用坦克的移动方法）
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')

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
        self.speed=50
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
