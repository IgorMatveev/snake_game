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
        self.default_win = ((0, 0), (self.rows - 1, self.rows - 1))
        self.food_gen = FoodGenerator(self)
        self.food_gen.create_some_food()
    
    def draw(self):
        """Рисует текущее состояние мира и объектов в нём"""
        pass
    
    def get_coords_from_act(self, coords, action):
        """Вычисляет новую координату объекта по действию пользователя"""
        pass
    
    class FoodGenerator():
        """Генератор еды"""
        
        def __init__(self, world, food_number=1):
            """Создает генератор"""
            self.world = world
            self.fd_num = food_number
        
        def create_some_food(self, window=None):
            """Создает еду"""
            window = window if window else self.world.default_win
            # TODO: генерировать n={self.fd_num} случайных неповторяющихся целочисленных 
            #       координат в рамках окна={window} и положить их в {self.world.food}
            self.world.NO_FOOD = False
    
        def delete_food(self, fd_coords):
            """Удаляет еду из мира"""
            self.world.food.remove(fd_coords)
            if not self.world.food:
                self.world.NO_FOOD = True


class Snake():
    """Змейка
Перемещается, ест еду. Если кусает своё тело или хвост, то умирает.
Хранит своё состояние в FIFO-очереди, в которой лежат относительные координаты квадтратов мира."""   
    
    def __init__(self, game, world, start_coords):
        """Создает змейку"""
        self.game = game
        self.world = world
        self.body_coords = type(self).FIFO(start_coords)
    
    @property
    def head(self):
        return self.body_coords.queue[-1]
    
    @property
    def tail(self):
        return self.body_coords.queue[:-1]
    
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
        action = self.game.get_move_act()
        new_coord = self.world.get_coords_from_act(self.head, action)
        if new_coord in self.world.food:
            self.body_coords.expand(new_coord)
            self.world.food_gen.delete_food(new_coord)
        else:
            self.body_coords.put(new_coord)
            if not self.selfcheck():
                self.status = 'DIEING'
    
    def selfcheck(self):
        """Проверяет своё состояние: не укусила ли свой хвост"""
        return not self.head in self.tail


class Game():
    """Игра Змейка
Создает, запускает и контролирует игру, захватывает действия пользователя"""
    
    def __init__(self):
        """Создает игру"""
        pass
    
    def _start(self):
        """Запускает (инициализирует игру)"""
        pass
    
    def play(self):
        """Контролирует игру"""
        pass
        
    def get_move_act(self):
        """Возвращает действие управления змейкой"""
        pass
