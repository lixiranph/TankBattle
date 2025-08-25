'''
v1.13
    完善子弹类的发射功能
    tank 发射子弹 ——>产生一颗子弹
'''
import pygame
import time
import random
_display = pygame.display
version='v1.13'
COLOR_RED = pygame.Color(255, 0, 0)
COLOR_BLACK = pygame.Color(0, 0, 0)
#游戏主窗口
class MainGame():
    window = None
    Screen_height = 500
    Screen_width = 800
    #创建我方坦克
    TANK_P1=None
    EnemyTank_list=[]#存储所有敌方坦克
    EnemyTank_count=5#创建敌方坦克的数量
    Bullet_list=[] #创建我方子弹列表
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
        #？创建敌方坦克
        self.createEnemyTank()
        clock = pygame.time.Clock()# ← 新增：帧率控制
        #让窗口持续刷新操作
        while True:
            #给窗口完成一个填充颜色
            MainGame.window.fill(COLOR_BLACK)
            #在循环中持续完成事件的获取
            self.getEvents()
            #将绘制文字得到的画布，粘贴到窗口中
            self.handleContinuousMove()  # ← 新增：每帧处理长按连续移动
            MainGame.window.blit(self.getTextSurface(f'剩余敌方坦克{len(MainGame.EnemyTank_list)}辆'),(5,5))
            #将我方坦克加入到窗口中
            MainGame.TANK_P1.displayTank()
            #循环展示敌方坦克
            self.blitEnemyTank()
            #根据坦克开关状态调用坦克的移动方法
            # if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
            #     MainGame.TANK_P1.move()
            #调用渲染子弹列表的方法
            self.blitBullet()
            #窗口的刷新
            _display.update()
            clock.tick(60)  # ← 用 tick 控帧，代替 time.sleep
    def createEnemyTank(self):
        MainGame.EnemyTank_list.clear()

        # 允许生成的纵向区域（敌人一般从上方进入）e
        TOP_MIN, TOP_MAX = 40, 180
        GAP = 12  # 敌人与敌人/我方之间的最小间距（像素）
        MAX_TRIES = 500  # 最多尝试放置次数，避免死循环
        tries = 0
        while len(MainGame.EnemyTank_list) < MainGame.EnemyTank_count and tries < MAX_TRIES:
            tries += 1
            speed = random.randint(1, 2)

            # 先“临时”创建一个敌人，拿到它的 rect 尺寸
            e = EnemyTank(0, 0, speed)
            e.rect.left = random.randint(0, MainGame.Screen_width - e.rect.width)
            e.rect.top = random.randint(TOP_MIN, min(TOP_MAX, MainGame.Screen_height - e.rect.height))

            # 用 inflate 给每个对象扩一圈 GAP 做安全间距
            cand = e.rect.inflate(GAP, GAP)

            # 先与我方坦克判定
            if cand.colliderect(MainGame.TANK_P1.rect.inflate(GAP, GAP)):
                continue

            # 再与已有的敌人判定
            conflict = False
            for other in MainGame.EnemyTank_list:
                if cand.colliderect(other.rect.inflate(GAP, GAP)):
                    conflict = True
                    break
            if conflict:
                continue

            # 位置安全，收下
            MainGame.EnemyTank_list.append(e)

        if len(MainGame.EnemyTank_list) < MainGame.EnemyTank_count:
            print(f'仅生成 {len(MainGame.EnemyTank_list)} 个敌人（空间不足或达到尝试上限）')
    #将坦克加入到窗口中
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            eTank.displayTank()
            eTank.randMove()
    #将子弹加入到窗口中
    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            '''---GPT提供的方法'''
            # 出屏就移除
            if (bullet.rect.right < 0 or bullet.rect.left > MainGame.Screen_width or
                bullet.rect.bottom < 0 or bullet.rect.top > MainGame.Screen_height):
                MainGame.Bullet_list.remove(bullet)
                continue
            bullet.displayBullet()
            '''---GPT提供的方法'''
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
                p1.direction = 'L'
                pressed_any = True
            elif keys[pygame.K_RIGHT]:
                p1.direction = 'R'
                pressed_any = True
            elif keys[pygame.K_UP]:
                p1.direction = 'U'
                pressed_any = True
            elif keys[pygame.K_DOWN]:
                p1.direction = 'D'
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
                    print('坦克向左掉头，并移动')
                elif event.key == pygame.K_RIGHT:
                    MainGame.TANK_P1.direction = 'R'
                    print('坦克向右掉头，并移动')
                elif event.key == pygame.K_UP:
                    MainGame.TANK_P1.direction = 'U'
                    print('坦克向上掉头，并移动')
                elif event.key == pygame.K_DOWN:
                    MainGame.TANK_P1.direction = 'D'
                    print('坦克向下掉头，并移动')
                elif event.key == pygame.K_SPACE:
                    print('发射子弹')
                    #产生一颗子弹
                    m=Bullet(MainGame.TANK_P1)
                    #将子弹加入到子弹列表
                    MainGame.Bullet_list.append(m)
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
            'U': pygame.image.load(r'Mytank/p1tankU.gif').convert_alpha(),
            'D': pygame.image.load(r'Mytank/p1tankD.gif').convert_alpha(),
            'L': pygame.image.load(r'Mytank/p1tankL.gif').convert_alpha(),
            'R': pygame.image.load(r'Mytank/p1tankR.gif').convert_alpha()
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
        return Bullet(self)
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
    def __init__(self, left, top, speed):
        #图片集
        #方向
        #图片
        #rect
        #速度
        #live
        super().__init__(left, top)
        self.images = {
            'U': pygame.image.load(r'EnemyTank\P1\enemy1U.gif').convert_alpha(),
            'D': pygame.image.load(r'EnemyTank\P1\enemy1D.gif').convert_alpha(),
            'L': pygame.image.load(r'EnemyTank\P1\enemy1L.gif').convert_alpha(),
            'R': pygame.image.load(r'EnemyTank\P1\enemy1R.gif').convert_alpha()
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]
        # 坦克所在的区域 Rect类型
        self.rect = self.image.get_rect()
        # 指定坦克初始化位置 分别距X，Y轴的位置
        self.rect.left = left
        self.rect.top = top
        # 新增速度属性
        self.speed = speed
        # 新增属性：坦克的移动开关
        self.stop = True
        # 新增步数属性
        self.step = 50
    def randDirection(self):
        num=random.randint(1,4)
        if num==1:
            return 'U'
        elif num==2:
            return 'D'
        elif num==3:
            return 'L'
        elif num==4:
            return 'R'
    # def displayEnemyTank(self):
    #     super().displayTank()
    def randMove(self):
        if self.step<=0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -=1
class Bullet():
    def __init__(self,tank):
        #图片
        self.image =pygame.image.load(r'bullet\tankmissile.gif')
        #方向(取决于坦克的方向)
        self.direction=tank.direction
        #位置
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.centerx = tank.rect.centerx
            self.rect.bottom   = tank.rect.top     # 子弹底对齐坦克顶
        elif self.direction == 'D':
            self.rect.centerx = tank.rect.centerx
            self.rect.top     = tank.rect.bottom   # ✅ 放到坦克底边外
        elif self.direction == 'L':
            self.rect.right   = tank.rect.left     # ✅ 放到坦克左侧外
            self.rect.centery = tank.rect.centery
        elif self.direction == 'R':
            self.rect.left    = tank.rect.right    # ✅ 放到坦克右侧外
            self.rect.centery = tank.rect.centery
        #速度
        self.speed=7
    def move(self):
        '''移动子弹的方法'''
        pass
    def displayBullet(self):
        '''展示子弹的方法'''
        MainGame.window.blit(self.image, self.rect)
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
