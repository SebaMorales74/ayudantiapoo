import pygame, random
import os
pygame.init()


size = width, height = 800,600
ventana = pygame.display.set_mode(size)
fps = pygame.time.Clock()

class Jugador:
    def __init__(self):
        self.imagen = pygame.image.load(r"C:/GitHub/ayudantiapoo/Ejemplo Pygame/endlessAutomovil/autito.png").convert_alpha()
        self.hitbox = self.imagen.get_rect()
        self.carriles = [260,400]
        self.x = 120
        self.y = 380
        self.hitbox.center = (self.x,self.y)
        self.score = 0
        self.speed = 5
        self.gameover = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
        
        if self.hitbox.y<self.carriles[0]:
            self.hitbox.y = self.carriles[0]
        if self.hitbox.y>self.carriles[1]:
            self.hitbox.y = self.carriles[1]
        
        ventana.blit(self.imagen,self.hitbox)

class Enemigo:
    def __init__(self):
        self.imagen = pygame.image.load(r"C:/GitHub/ayudantiapoo/Ejemplo Pygame/endlessAutomovil/autito_blanco.png").convert_alpha()
        self.hitbox = self.imagen.get_rect()
        self.carriles = [320,430]
        self.x = width+300
        self.y = random.choice(self.carriles)
        self.hitbox.center = (self.x,self.y)

    def move(self, player):
        self.hitbox.x -= player.speed

        if self.hitbox.x < -300:
            self.x = width+300
            self.y = random.choice(self.carriles)
            self.hitbox.center = (self.x,self.y)

        self.collide = self.hitbox.colliderect(player.hitbox)
        
        if self.collide == True:
            print("ME CHOCASTE PUTA")

        ventana.blit(self.imagen,self.hitbox)  

class Moneda:
    def __init__(self):
        self.imagen = pygame.image.load(r"C:/GitHub/ayudantiapoo/Ejemplo Pygame/endlessAutomovil/moneda de 500.png").convert_alpha()
        self.hitbox = self.imagen.get_rect()
        self.carriles = [430,320]
        self.x = width+300
        self.y = random.choice(self.carriles)
        self.hitbox.center = (self.x,self.y)

    def move(self,player):

        self.hitbox.x -= player.speed

        self.collide = self.hitbox.colliderect(player.hitbox)

        if self.hitbox.x < -300:
            self.x = width+300
            self.y = random.choice(self.carriles)
            self.hitbox.center = (self.x,self.y)
        
        if self.collide == True:
            self.x = width+300
            self.y = random.choice(self.carriles)
            self.hitbox.center = (self.x,self.y)
            player.score += 1
            player.speed += 1

        ventana.blit(self.imagen,self.hitbox)

class Carretera:
    def __init__(self,limite=1):
        self.imagen = pygame.image.load(r"C:/GitHub/ayudantiapoo/Ejemplo Pygame/endlessAutomovil/carretera.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,(width+200,height+200))
        self.hitbox = self.imagen.get_rect()
        self.limite = -limite
        self.speed = 20
    
    def move(self):
        self.hitbox.x -= self.speed

        if self.hitbox.x < -200:
            self.hitbox.x = 0
        ventana.blit(self.imagen,self.hitbox)

player = Jugador()
enemigo = Enemigo()
moneda = Moneda()
carretera = Carretera()

while True:
    fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    ventana.fill((255,255,255))

    carretera.move()
    moneda.move(player)
    enemigo.move(player)
    player.move()
    
    pygame.display.update()
