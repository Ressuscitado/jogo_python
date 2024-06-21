#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_option):
        self.window: Surface = window
        self.name = name
        self.mode = menu_option  # Opção do Menu
        #  Entidades podem se mover, por isso devido ao Paralaxe escolhemos usar entidade
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        #  Usamos um position ja definido em factory para n ter q repetir para todas as img
        #  visto que todas terão a mesma posição

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass

