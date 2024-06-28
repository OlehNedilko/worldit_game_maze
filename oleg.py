import pygame
import os

pygame.init()

monitor = pygame.display.set_mode((500, 500))

clock = pygame.time.Clock()

hero = pygame.Rect(50, 50, 50, 50)

right = False
left = False
up = False
down = False

polnii_pyt = os.path.dirname(__file__)
kartinki_koroche = os.path.abspath(polnii_pyt + "/textures")
bush = pygame.image.load(kartinki_koroche + "/bush.png")
geometry_dash = pygame.image.load(kartinki_koroche + "/geroi_kubik.png")
finish = pygame.image.load(kartinki_koroche + "/hehehehafinish.png")
pol = pygame.image.load(kartinki_koroche + "/prosto_pol.png")


#bush = 1
#geometry_dash = 2
#finish = 3
#pol = 4


x = 0
y = 0

teksuri = [   #10 x 10
    [1,1,1,1,1,1,1,1,1,1], 
    [4,4,4,4,1,1,1,1,1,1], 
    [4,4,4,4,1,1,1,1,1,1], 
    [1,1,4,4,1,1,1,1,1,1], 
    [1,1,4,4,1,1,1,1,1,1], 
    [1,1,4,4,1,1,1,1,1,1], 
    [1,1,4,4,4,4,4,4,1,1], 
    [1,1,4,4,4,4,4,4,1,1], 
    [1,1,1,1,1,1,4,4,1,1], 
    [1,1,1,1,1,1,3,3,1,1]  
]

kvadrati = []
kvadrat_textura = []

bad_textures = []
good_textures = []

for teksturaaa in teksuri:
    for i in teksturaaa:
        kvadratik = pygame.Rect(x, y, 50, 50)
        kvadrati.append(kvadratik)
        kvadrat_textura.append(i)
        if i == 1:
            bad_textures.append(kvadratik)
        if i == 3:
            good_textures.append(kvadratik)
        x += 50
    y += 50
    x = 0

kvadrati_len = len(kvadrati)

game_work = True

font = pygame.font.SysFont("Calibri", 50)
text = font.render("u win", True, (255, 255, 255))

while game_work:

    monitor.fill((255, 255, 255))
    
    pygame.draw.rect(monitor, (0, 0, 0), hero)


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_work = False   
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_w:
                up = True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_d:
                right = True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_s:
                down = True
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_a:
                left = True  
        
#---------------------------------------------------------------------------#        
        
        
        
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_w:
                up = False
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_d:
                right = False
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_s:
                down = False
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_a:
                left = False
    
    
    
    for i in range(kvadrati_len):
        if kvadrat_textura[i] == 1:
            monitor.blit(bush, kvadrati[i])
        if kvadrat_textura[i] == 2:
            monitor.blit(geometry_dash, kvadrati[i])
        if kvadrat_textura[i] == 3:
            monitor.blit(finish, kvadrati[i])
        if kvadrat_textura[i] == 4:
            monitor.blit(pol, kvadrati[i])
    
    monitor.blit(geometry_dash, hero)

    for bad in bad_textures:
        if hero.colliderect(bad):
            hero.x = 50
            hero.y = 50
        
    for good in good_textures:
        if hero.colliderect(good):
            monitor.fill((0, 0, 0))
            monitor.blit(text, (210, 150))
            up = False
            down = False
            right = False
            left = False

    if up == True:
        hero.y -= 5
    if down == True:
        hero.y += 5
    if right == True:
        hero.x += 5
    if left == True:
        hero.x -= 5
    
    # if hero.colliderect(bush):
    #     print("умер")
    # if hero.colliderect(finish):
    #     print("прошел")
    
    pygame.display.flip()
    clock.tick(60)