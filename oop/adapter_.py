#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 14:04:12 2022

@author: ka
"""

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