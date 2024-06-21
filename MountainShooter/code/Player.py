#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        # Se usarmos o ELIF não poderia apertar todas teclas de uma vez, por isso o IF
        # ELIF é se for verdadeiro os outros não importa
        pressed_key = pygame.key.get_pressed()  # Não é ao clicar, é ao manter pressionado
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]]and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

