import sys, pygame, util
from pygame.locals import *
from cat import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

def game():
    pygame.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Catpy" )
    background_image = util.cargar_imagen('fondo.jpg');
    background_image = pygame.transform.scale (background_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    obstaculo_image = util.cargar_imagen ('dos.png');
    obstaculo_image = pygame.transform.scale(obstaculo_image, (150, 100))
    obstaculo_rect = obstaculo_image.get_rect()
    obstaculo_rect.move_ip(SCREEN_WIDTH/2, 300)
    pygame.mouse.set_visible( False )
    cat = Cat()
    
    while True:       
        cat.update((SCREEN_WIDTH,SCREEN_HEIGHT))      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background_image, (0,0))
        screen.blit(cat.image, cat.rect)
        screen.blit(obstaculo_image, (SCREEN_WIDTH/2, 300))
        if cat.rect.colliderect(obstaculo_rect):
            cat.estado = 0
        pygame.display.update()
        pygame.time.delay(10)
        
      
if __name__ == '__main__':
      game()

