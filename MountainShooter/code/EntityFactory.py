#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_WIDTH


#  Usando o design Pattern FACTORY, usa uma classe chamada Factory, ela que irá produzir os
#  Filhos da classe abstrata e ao invocar o construtor dela ela sempre retorna
class EntityFactory:

    @staticmethod  # Faz parte da classe, mas é estático, n precisa instanciar
    def get_entity(entity_name: str, position=(0, 0)):  # pois todos BG irão para mesma posição
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg

