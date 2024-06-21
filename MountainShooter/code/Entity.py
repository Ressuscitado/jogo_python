#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        #  Sempre ao construir o REC de uma entidade devemos passar a posição
        self.speed = 0
    #  (No python temos que fazer essa importação ABC
    #  para usar classe abstrata, ela não vem nativa)
    #  Uma classe abstrata ABC não implementa nenhum método, só tem métodos
    #  abstratos por isso o uso do @abstractmethod

    @abstractmethod  # As classes filhas obrigatoriamente devem implementar os métodos de pai
    def move(self, ):
        pass

