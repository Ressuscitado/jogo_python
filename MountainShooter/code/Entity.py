#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame

from code.Const import ENTITY_HEALTH, ENTITY_SPEED, ENTITY_DAMAGE, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + self.name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        #  Sempre ao construir o REC de uma entidade devemos passar a posição
        self.speed = ENTITY_SPEED[self.name]
        #  (No python temos que fazer essa importação ABC
        #  para usar classe abstrata, ela não vem nativa)
        #  Uma classe abstrata ABC não implementa nenhum método, só tem métodos
        #  abstratos por isso o uso do @abstractmethod
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'None'

    @abstractmethod  # As classes filhas obrigatoriamente devem implementar os métodos de pai
    def move(self, ):
        pass

