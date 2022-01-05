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
    
    def __init__(self, x, y=None):
        if y != None:
            self.x=x
            self.y=y
        else:
            self.x=x[0]
            self.y=x[1]
   
    def __add__(self, obj):
         """сумма векторов"""   
         return Vec2d(self.x + obj.x, self.y + obj.y)
     
    def __sub__(self, obj):
        """разность векторов"""
        return Vec2d(self.x - obj.x, self.y - obj.y)
    
    def __mul__(self, k):
        """произведение на число"""
        if isinstance(k, Vec2d):
            return self.x * k.x + self.y * k.y
        return Vec2d(self.x * k, self.y * k)
    
    def int_pair(self):
        """возвращает кортеж из двух целых чисел"""
        return (int(self.x), int(self.y))  
        
    def len(self, x):
        """возвращает длину вектора"""
        return Vec2d(math.sqrt(x[0] * x[0] + x[1] * x[1]))


    def vec(self, obj):
        """возвращает пару координат, определяющих вектор (координаты точки конца вектора),
        координаты начальной точки вектора совпадают с началом системы координат (0, 0)"""
        return obj - self
    
class Polyline():
    
    """методами отвечающими за добавление в ломаную точки (Vec2d) 
    c её скоростью, пересчёт координат точек (set_points) и отрисовку
    ломаной (draw_points). Арифметические действия с векторами должны
    быть реализованы с помощью операторов, а не через вызовы
    соответствующих методов."""
    
    
    def __init__(self, points:list=[], speeds:list=[]):
        self.points=points
        self.speeds=speeds
        
    def delete(self):
        try:
            self.points.pop()
            self.speeds.pop()
        except:
            None
            
    def add_speed(self, a=0.5):
        for i in range(0, len(self.speeds)):
            if self.speeds[i].x > 0:
                self.speeds[i].x += a
            else:
                self.speeds[i].x -= a
                
            if self.speeds[i].y > 0:
                self.speeds[i].y += a
            else:
                self.speeds[i].y -= a
                
    def dwn_speed(self, a=0.5):
        for i in range(0, len(self.speeds)):
            if self.speeds[i].x > 0:
                self.speeds[i].x -= a
            else:
                self.speeds[i].x += a
                
            if self.speeds[i].y > 0:
                self.speeds[i].y -= a
            else:
                self.speeds[i].y += a
            
    def append(self,points,speeds):
        self.points.append(points)
        self.speeds.append(speeds)
        
    def draw_points(self, points=None, style="points", width=3, color=WHITE):
        """функция отрисовки точек на экране"""
        if style == "line":
            for p_n in range(-1, len(points) - 2):
                pygame.draw.line(gameDisplay,
                                 color,
                                 points[p_n + 1].int_pair(),
                                 points[p_n].int_pair(),
                                 3)
           # pygame.draw.lines(gameDisplay, color, True, [i.int_pair() for i in self.points],7) 
    
        elif style == "points":
           # print(self.points)
            for p in self.points:
                pygame.draw.circle(gameDisplay, color,
                                   p.int_pair(), width)
    
    
    def set_points(self):
        """функция перерасчета координат опорных точек"""
        for p in range(len(self.points)):
            self.points[p] += self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(- self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)
                


class Knot(Polyline):
    
    """Реализовать класс Knot (наследник класса Polyline), в котором 
    добавление и пересчёт координат инициируют вызов функции
    get_knot для расчёта точек кривой по добавляемым «опорным» точкам [2]."""
    
    
    def __init__(self, count):
        
        super().__init__(points=[], speeds=[])
        self.count = count
        
    def append(self, points, speed):
        super().append(points, speed)
        self.get_knot()
    
    def delete(self):
        try:
            self.points.pop()
            self.speeds.pop()
        except:
            None
            
    def add_speed(self, a=0.5):
        for i in range(0, len(self.speeds)):
            if self.speeds[i].x > 0:
                self.speeds[i].x += a
            else:
                self.speeds[i].x -= a
                
            if self.speeds[i].y > 0:
                self.speeds[i].y += a
            else:
                self.speeds[i].y -= a
                
    def dwn_speed(self, a=0.5):
        for i in range(0, len(self.speeds)):
            if self.speeds[i].x > 0:
                self.speeds[i].x -= a
            else:
                self.speeds[i].x += a
                
            if self.speeds[i].y > 0:
                self.speeds[i].y -= a
            else:
                self.speeds[i].y += a
            
    def get_knot(self, s=0.5, a=1):
        
        if len(self.points) < 3:
            return []
        res = []
        for i in range(-2, len(self.points) - 2):
            ptn = []
            ptn.append((self.points[i]* s) + (self.points[i + a] * s))
            ptn.append(self.points[i + a])
            ptn.append((self.points[i + a] * s )+ (self.points[i + 2] * s))
            res.extend(self.get_points(ptn))
        return res
    

# =======================================================================================
# Функции, отвечающие за расчет сглаживания ломаной
# =======================================================================================
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
       # print(((points[deg] * 1) + (self.get_point(points, alpha, deg - 1) * (1 - 0.5))))
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)
    
    
    def get_points(self, base_points):
        alpha = 1 / self.count
        res = []
        for i in range(self.count):
            res.append(self.get_point(base_points, i * alpha))
        return res
    
  
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
        ("L", "Add lines"),
        ("A", "Up speeds"),
        ("S", "Dwn speeds"),
        ("", ""),
        (str(steps), "Current points")
        )

    pygame.draw.lines(gameDisplay, (255, 50, 50, 255), True, [
        (0, 0), (SCREEN_DIM[0], 0), SCREEN_DIM, (0, SCREEN_DIM[1])], 5)
    for i, text in enumerate(data):
        gameDisplay.blit(font1.render(
            text[0], True, (128, 128, 255)), (100, 100 + 30 * i))
        gameDisplay.blit(font2.render(
            text[1], True, (128, 128, 255)), (200, 100 + 30 * i)) 
# =======================================================================================
# Основная программа
# =======================================================================================
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")
    steps = 35
    working = True
    polyline = Polyline()
    knot = Knot(steps)
    show_help = False
    pause = True
    new=False
    hue = 0
    color = pygame.Color(0)
    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    polyline = Polyline()
                    knot = Knot(steps)
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                    knot.count=steps
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0
                    knot.count=steps
                if event.key == pygame.K_a:
                    polyline.add_speed(0.1)
                    knot.add_speed(0.1)
                if event.key == pygame.K_s:
                    polyline.dwn_speed(0.1)
                    knot.dwn_speed(0.1)
                if event.key == pygame.K_l:
                    new=True
                    poly=Polyline()
                    poly.speeds = polyline.speeds.copy()
                    poly.points = polyline.points.copy()
                if event.key == pygame.K_DELETE:
                    knot.delete()
                    polyline.delete()
                    if new:
                        polyline.draw_points((knot.get_knot(0.5, 0)), style = "line")
                        knot.draw_points(knot.get_knot(), 3, color)
            if event.type == pygame.MOUSEBUTTONDOWN:
                polyline.append(Vec2d(event.pos), Vec2d(random.random() * 2, random.random() * 2))
                knot.append(Vec2d(event.pos), Vec2d(random.random() * 2, random.random() * 2))
        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        #polyline.draw_points()
        if new:
            poly.draw_points((knot.get_knot(0.5, 2)), style = "line", color=WHITE)
        polyline.draw_points(knot.get_knot(),style = "line", color=color)
        polyline.draw_points(knot.get_knot(),style = "points")
        if not pause:
            polyline.set_points()
            knot.set_points()
        if show_help:
            draw_help()
        pygame.display.flip()
    pygame.display.quit()
    pygame.quit()