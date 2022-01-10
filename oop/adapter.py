#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 14:04:12 2022

@author: ka
"""
from abc import abstractmethod

class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1 # Источники света
        self.map[5][2] = -1 # Стены
    
    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)
        
        
class LightProcessor():
    
    @abstractmethod
    def lighten(self, grid):
        pass
        
class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []
        
    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
    
    def set_lights(self, lights):
        '''
        устанавливает массив источников света с заданными координатами и просчитывает освещение
        '''
        self.lights = lights
        self.generate_lights()
    
    def set_obstacles(self, obstacles):
        '''
        устанавливает препятствия 

        '''
        self.obstacles = obstacles
        self.generate_lights()
        
    def generate_lights(self):
        '''
        рассчитывает освещенность с учетом источников и препятствий.
        '''
        return self.grid.copy()


class MappingAdapter():
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        
        lights=[]
        obstacles=[]
        
        self.adaptee.set_dim((len(grid[0]), len(grid)))
        
        for i in range(0, len(grid)):
            for s in range(0, len(grid[i])):
                if grid[i][s]==0:
                    continue
                elif grid[i][s]==-1:
                    obstacles.append((s, i))
                elif grid[i][s]==1:
                    lights.append((s, i))
                    
        self.adaptee.set_lights(lights)
        self.adaptee.set_obstacles(obstacles)
        return self.adaptee.generate_lights()

if __name__=='__main__':
    system = System()
    light = Light((0, 0))
    adapter = MappingAdapter(light)
    system.get_lightening(adapter)
    system.lightmap