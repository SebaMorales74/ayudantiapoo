import pygame
import Personajes

pygame.init()

size = width, height = 800, 600
ventana = pygame.display.set_mode(size)
fps = pygame.time.Clock()

class Player:

    def __init__(self,
                 alto=20,
                 ancho=20,
                 velocidad=5,
                 color=(255, 255, 255),
                 image="./assets/sprites/firedude.png",
                 derecha=pygame.K_d,
                 izquierda=pygame.K_a,
                 arriba=pygame.K_w):

        self.hitbox = pygame.Rect(0, 0, alto, ancho)
        self.hitbox.center = ventana.get_rect().center
        self.image = pygame.image.load("./assets/sprites/" + image)
        self.image = pygame.transform.scale(self.image, (alto, ancho))
        self.image.set_colorkey((255, 255, 255))
        self.velocidad = velocidad
        self.color = color
        self.gravedad = 0.5
        self.accVertical = 0
        self.derecha = derecha
        self.izquierda = izquierda
        self.arriba = arriba
        self.orientation = "right"
        self.saltos = 0

    def move(self):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[self.derecha]:
            dx += self.velocidad
            self.orientation = "right"
        if keys[self.izquierda]:
            dx -= self.velocidad
            self.orientation = "left"

        if self.hitbox.bottom < 600:
            self.accVertical += self.gravedad
        else:
            self.accVertical -= self.gravedad

        dy += self.accVertical

        for tile in world.tile_list:
            if tile.colliderect(self.hitbox.x, self.hitbox.y + dy,
                                self.hitbox.width, self.hitbox.height):
                dy = 0
                self.accVertical = 0
                self.saltos = 2
            if tile.colliderect(self.hitbox.x + dx, self.hitbox.y,
                                self.hitbox.width, self.hitbox.height):
                dx = 0

        self.hitbox.x += dx
        self.hitbox.y += dy

        if self.orientation == "right":
            # pygame.draw.rect(ventana, self.color, self.hitbox)
            ventana.blit(self.image, self.hitbox)
        elif self.orientation == "left":
            # pygame.draw.rect(ventana, self.color, self.hitbox)
            ventana.blit(pygame.transform.flip(self.image, True, False),
                         self.hitbox)


class World:

    def __init__(self, data=[], color=(0, 0, 0)):
        self.tile_list = []

        self.color = color
        self.tileSize = 32

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    self.tile = pygame.Rect(0, 0, self.tileSize, self.tileSize)
                    self.tile.x = col_count * self.tileSize
                    self.tile.y = row_count * self.tileSize
                    self.tile_list.append(self.tile)
                col_count += 1
            row_count += 1

    def draw(self):
        ventana.fill(self.color)
        for tile in self.tile_list:
            pygame.draw.rect(ventana, (173, 112, 71), tile)


world_map = [
    [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
        1
    ],
    [
        1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1
    ],
    [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1
    ],
]

world = World(world_map, (107, 95, 55))

jugador = Player(32, 48, 5, (255, 98, 0), "firedude.png", pygame.K_RIGHT,
                 pygame.K_LEFT, pygame.K_UP)
jugador2 = Player(32, 48, 5, (0, 98, 255), "waterchick.png", pygame.K_d,
                  pygame.K_a, pygame.K_w)

personajes = Personajes()

while True:
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == jugador.arriba and jugador.saltos > 0:
                jugador.accVertical = -10
            if event.key == jugador2.arriba and jugador2.saltos > 0:
                jugador2.accVertical = -10
    world.draw()

    jugador.move()
    jugador2.move()

    ventana.blit(
        pygame.font.SysFont("Arial", 20).render(
            "FPS: " + str('{:.0f}'.format(fps.get_fps())), True,
            (255, 255, 255)), (0, 0))

    pygame.display.flip()
