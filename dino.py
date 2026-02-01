import pygame, random, sys
pygame.init()
W, H = 800, 400
s = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)
dino = pygame.image.load("dino.png")
cactus = pygame.image.load("cactus.png")
ground = pygame.image.load("ground.gif")
dino = pygame.transform.scale(dino, (80, 80))
cactus = pygame.transform.scale(cactus, (60, 80))
ground = pygame.transform.scale(ground, (W, 100))
rect = dino.get_rect(topleft=(100, 280))
vel, g, jump = 0, 1.2, False
ob = [pygame.Rect(900, 300, 60, 80)]
score, speed, run = 0, 6, True
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE and not jump: vel, jump = -25, True
            if e.key == pygame.K_r and not run: run, score, ob, speed = True, 0, 
            [pygame.Rect(900, 300, 60, 80)], 6
    s.fill((255, 255, 255)); s.blit(ground, (0, 300))
    if run:
        vel += g; rect.y += vel
        if rect.y >= 280: rect.y, jump = 280, False
        for o in ob:
            o.x -= speed; s.blit(cactus, o)
            if rect.colliderect(o): run = False
            if o.x + 60 < rect.x and o.x > -100: score += 1
        if ob[-1].x < random.randint(300, 500): ob.append(pygame.Rect(900, 300, 60, 80))
        if ob[0].x < -100: ob.pop(0)
        s.blit(dino, rect)
        s.blit(font.render(f"Score:{score}", True, (0,0,0)), (20,20))
    else:
        s.blit(font.render(f"Game Over! {score}", True, (0,0,0)), (300,150))
        s.blit(font.render("Press R", True, (0,0,0)), (350,200))
    pygame.display.flip(); clock.tick(60)
