import numpy as np
import pygame as pg
import tkinter as tk

class World():
    """Мир, в котором существует змейка.
Представляет из себя разбитую на квадраты облать окна (карты). В нём
могут существовать змейки, есть генератор еды для змеек."""
    
    rows = 20
    width = 500
    objs = []
    
    def __init__(self, game):
        """Создает мир"""
        pass
    
    def draw(self):
        """Рисует текущее состояние мира и объектов в нём"""
        pass


class Snake():
    """Змейка
Перемещается, ест еду. Если кусает своё тело или хвост, то умирает.
Хранит своё состояние в FIFO-очереди, в которой лежат относительные координаты квадтратов мира."""   
    
    def __init__(self, game, world, start_coords):
        """Создает змейку"""
        self.game = game
        self.world = world
        self.coords = type(self).FIFO(start_coords)
        pass
    
    class FIFO():
        """FIFO-очередь
Хранит соординаты положения змейки"""
        
        def __init__(self, default=None):
            self.queue = [default] if default else []
        
        def put(self, value):
            for i in range(len(self.queue)-1):
                self.queue[i] = self.queue[i+1]
            self.queue[-1] = value
        
        def expand(self, value):
            self.queue.append(value)
            
        def __repr__(self):
            return self.queue.__repr__()
    
    def draw(self):
        """Рисует змейку"""
        pass
    
    def move(self):
        """Перемещает змейку"""
        pass
    
    def selfcheck(self):
        """Проверяет своё состояние"""
        pass
    


class Game():
    """Игра Змейка
Создает, запускает и контролирует игру"""
    def __init__(self):
        """Создает игру"""
        pass
    
    def _start(self):
        """Запускает (инициализирует игру)"""
        pass
    
    def play(self):
        """Контролирует игру"""
