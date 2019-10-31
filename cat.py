import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Cat(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.imagenes = [util.cargar_imagen('cat_0.png'),
                                        util.cargar_imagen('cat_1.png'),
                                        util.cargar_imagen('cat_2.png'),
                                        util.cargar_imagen('cat_3.png'),
                                        util.cargar_imagen('cat_4.png'),
                                        util.cargar_imagen('cat_5.png'),
                                        util.cargar_imagen('cat_6.png'),
                                        util.cargar_imagen('cat_8.png')]
        self.cont = 0
        self.image = self.imagenes[self.cont]
        self.rect = self.image.get_rect()
        self.rect.move_ip(1,300)
        self.vel = [3,3]
        self.estado = 1
		
        
    def update(self,size):
        if self.estado == 1:
            teclas = pygame.key.get_pressed()
            if teclas[K_RIGHT]:
                self.vel[0] += 1
            if teclas[K_LEFT] and self.vel[0] > 1 :
                self.vel[0] -= 1
            self.rect.x = (self.rect.x + self.vel[0]) % size[0]
            self.cont = (self.cont + 1) % 8
            self.image = self.imagenes[self.cont]
        else:
            self.image = util.cargar_imagen('die.png')
        self.image = pygame.transform.scale(self.image,(150,100))
        self.rect.size = (128, 128)
        self.rect.y = size[1] - 128
