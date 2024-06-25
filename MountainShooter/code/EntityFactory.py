#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


#  Usando o design Pattern FACTORY, usa uma classe chamada Factory, ela que irá produzir os
#  Filhos da classe abstrata e ao invocar o construtor dela ela sempre retorna
class EntityFactory:

    @staticmethod  # Faz parte da classe, mas é estático, n precisa instanciar
    def get_entity(entity_name: str, position=(0, 0)):  # pois todos BG irão para mesma posição
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):  # Número de sprites que compõem o mapa
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Level2Bg':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT / 2 + 30))

            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))

            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0 + 40, WIN_HEIGHT - 40)))

