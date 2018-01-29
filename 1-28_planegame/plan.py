#导入pygame
import time
import random
import pygame
from pygame.locals import *
class Plane:
    def __init__(self,screen,name):
        self.name=name
        #设置要显示内容的窗口
        self.screen=screen
        self.image=pygame.image.load(self.imageName).convert()
        #用来保存玩家发射的所有导弹
        self.bulletList=[]
    def display(self):
        #更新飞机的位置
        self.screen.blit(self.image,(self.x,self.y))
        #存放需要删除的对象信息
        needDelItemList=[]
        #判断一下导弹的位置是否越界，如果是，那么就要删除这枚导弹
        for i in self.bulletList:
            if i.judge():
                needDelItemList.append(i)
        for i in needDelItemList:
            self.bulletList.remove(i)
        #更新飞机发射出的所有导弹的位置
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
    def sheBullet(self):
        newBullet=Bullet(self.x,self.y,self.screen,self.name)
        self.bulletList.append(newBullet)
class HeroPlane(Plane):
    def __init__(self,screen,name):
        #设置飞机默认的位置
        self.x=230
        self.y=600
        self.imageName='feiji\\hero.gif'
        super().__init__(screen,name)
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
    def moveLeft(self):
        self.x-=10
    def moveRight(self):
        self.x+=10
    def sheBullet(self):
        pass
class Bullet:
    def __init__(self,x,y,screen):
        self.image=pygame.image.load("feiji\\bullet.png").convert()
        self.x=x+40
        self.y=y-25
        self.screen=screen
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=2

if __name__=='__main__':
    #创建窗口
    screen=pygame.display.set_mode((480,890),0,32)
    pygame.image.load("C:\\Users\\assu\\PycharmProjects\\python学习打卡\\1-28_planegame\\feiji\\bg.png").convert()
    #不加这个win8 x64会未响应
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()


