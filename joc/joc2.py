import pygame
pygame.init()
w,h=800,600
s=pygame.display.set_mode((w,h))
p=pygame.Surface((w*0.2,10))
p.fill((255,255,255))
b=pygame.Surface((5,5))
b.fill((255,255,255))
bx=w//2
by=h//2
bs=1
px=h-50
py=h-50
ps=5
clock=pygame.time.Clock()
while True:
    s.fill((0,0,0))
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            exit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        px-=ps
    if keys[pygame.K_RIGHT]:
        px+=ps
    if keys[pygame.K_SPACE]:
        bx,by=w//2,h//2
        bs=1
    bx+=bs
    if bx<0 or bx>s.get_width():
        bs*=-1
    if by<0:
        bs*=-1
    if by>py and by<py+p.get_height() and bx>px and bx<px+p.get_width():
        if bx<px+p.get_width()//2:
            bs=-1
        else:
            bs=1
        bs*=-1
    s.blit(p,(px,py))
    s.blit(b,(bx,by))
    pygame.display.flip()
    clock.tick(100)
