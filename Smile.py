#coding=utf-8

import pygame
pygame.init()
from pygame.locals import *
#создание окна
width = 800
height = 600
win = pygame.display.set_mode((width, height))
time = pygame.time.Clock()
#создание заголовка
pygame.display.set_caption("Object")
#переменные для персонажа
x = 50
y = 200
radius = 50
speedx = 5
speedy = 5
keepGoing = True
green = (0, 255, 255)
isJump = False
jumpCount = 10
left = False
right = False
animCount = 0
pic = pygame.image.load('CrazySmile.bmp')  #картинка с компьютера
#back graund
bg = (0, 0, 0)
#подгрузка фона и анимации
def drawWindow():
    global animCount
#    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

#цикл для постонной работы приложения / игровой цикл
run = True
while run:
    win.fill(bg)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x > 0 and x + pic.get_width() < width:
        speedx = speedx
    else:
        speedx = -speedx
    if y > 0 and y + pic.get_width() < height:
        speedy = speedy
    else:
        speedy = -speedy
    x += speedx
    y += speedy
    win.blit(pic, (x,y)) #рисует изображение на экране
    pygame.display.update()

    time.tick(30)
pygame.quit()
