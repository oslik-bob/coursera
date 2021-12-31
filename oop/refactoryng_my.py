#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
К дополнительным задачам относятся:
    реализовать возможность удаления «опорной» точки из кривой, 
    реализовать возможность отрисовки на экране нескольких кривых, 
    реализовать возможность ускорения/замедления скорости движения кривой(-ых).
"""

import pygame
import random
import math

SCREEN_DIM = (800, 600)
MENU_COLLOR = (128, 128, 255)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
BLACK = (  0,   0,   0)
HELP_COLLOR = (  50,   50,   50)


class Vec2d:
    
    """
    В классе определить методы для основных математических операций,
    необходимых для работы с вектором:
        Vec2d.__add__ (сумма), 
        Vec2d.__sub__ (разность), 
        Vec2d.__mul__ (произведение на число).
    Добавить возможность вычислять длину вектора с использованием функции 
    len(a) и метод int_pair, который возвращает кортеж из двух целых чисел
    (текущие координаты вектора)."""
    
    def __init__(self, x, y):
        self.x=x
        self.y=y
   
    def __add__(self, obj):
         """сумма векторов"""     
         return self.x + obj.x, self.y + obj.y
     
    def __sub__(self, obj):
        """разность векторов"""
        return self.x - obj.x, self.y - obj.y
    
    def __mul__(self, k):
        """произведение на число"""
        return self.x * k, self.y * k
    
    def int_pair(self, vector):
        """возвращает кортеж из двух целых чисел"""
        return (int(vector[0]), int(vector[1]))  
        
    def length(x):
        """возвращает длину вектора"""
        return math.sqrt(x[0] * x[0] + x[1] * x[1])


    def vec(self, obj):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return obj - self
    
class Polyline(Vec2d):
    
    """методами отвечающими за добавление в ломаную точки (Vec2d) 
    c её скоростью, пересчёт координат точек (set_points) и отрисовку
    ломаной (draw_points). Арифметические действия с векторами должны
    быть реализованы с помощью операторов, а не через вызовы
    соответствующих методов."""
    
    
    def __init__(self, points:list=[], speeds:list=[]):
        self.points=points
        self.speeds=speeds
        
    
    def append(self,pos):
        self.points.append(pos)
        self.draw_points()
        
    def draw_points(self, style="points", width=3, color=WHITE):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(
                    gameDisplay, color,
                    (self.int_pair(self.points[p_n]), 
                     self.int_pair(self.points[p_n + 1])), width)
    
        elif style == "points":
           # print(self.points)
            for p in self.points:
                
                pygame.draw.circle(gameDisplay, color,
                                   self.int_pair(p), width)
                print(self.int_pair(p))
    
    
    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (speeds[p][0], -self.speeds[p][1])
                

    
class Knot(Polyline):
    
    """Реализовать класс Knot (наследник класса Polyline), в котором 
    добавление и пересчёт координат инициируют вызов функции
    get_knot для расчёта точек кривой по добавляемым «опорным» точкам [2]."""
    
    
    def __init__(self,count):
        
        super().__init__(points=[], speeds=[])
        self.count = count
        
    def append(self, pos):
        super().append(pos)
            
    def get_knot(self):
        
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append((self.points[i] + self.points[i + 1]) * 0.5)
            ptn.append(self.points[i + 1])
            ptn.append((self.points[i + 1] + self.points[i + 2]) * 0.5)
    
            res.extend(get_points(ptn, self.count))
        return res
    
    pass

def draw_help():
    """функция отрисовки экрана справки программы"""
    gameDisplay.fill(HELP_COLLOR)
    font1 = pygame.font.SysFont("courier", 24)
    font2 = pygame.font.SysFont("serif", 24)
    data = (
        ("F1", "Show Help"),
        ("R", "Restart"),
        ("P", "Pause/Play"),
        ("Num+", "More points"),
        ("Num-", "Less points"),
        ("", ""),
        (str(steps), "Current points")
        )

    pygame.draw.lines(gameDisplay, (255, 50, 50), True, [
        (0, 0), (SCREEN_DIM[0], 0), SCREEN_DIM, (0, SCREEN_DIM[1])], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i)) 



# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
def get_point(points, alpha, deg=None):
    if deg is None:
        deg = len(points) - 1
    if deg == 0:
        return points[0]
    return (points[deg] * alpha) + (get_point(points, 
                                              alpha, deg - 1) * 1 - alpha)


def get_points(base_points, count):
    alpha = 1 / count
    res = []
    for i in range(count):
        res.append(get_point(base_points, i * alpha))
    return res

def exits():
    pygame.display.quit()
    pygame.quit()
# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 1
    working = True
    points = Knot(steps)
    speeds = []
    show_help = False
    pause = False

    hue = 0
    color = pygame.Color(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exits()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exits()
# =============================================================================
#                 if event.key == pygame.K_r:
# 
#                     points = []
# 
#                     speeds = []
# =============================================================================
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        draw_points=Polyline()
        #draw_points(get_knot(points, steps), "line", 3, color)
        if not pause:
            draw_points.set_points()
        if show_help:
            draw_help()

        pygame.display.flip()
