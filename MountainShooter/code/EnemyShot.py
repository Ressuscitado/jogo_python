from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):  # significa que é filha de entidade

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

