import pygame
import random
import math

pygame.init()
FPS=60
WIDTH,HEIGHT=800,800
ROWS=4
COLS=4
Rect_height=HEIGHT//ROWS
Rect_width=WIDTH//COLS
Outline_Color=(187,173,160)
Outline_Thickness=10
Background_Color=(205,192,180)
Font_Color=(119,110,101)
FONT=pygame.font.SysFont("comicsans",60,bold=True)
MOV_VEL=20
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tiles combining game (2048)")
def drawGrid(window):
    for row in range(1,ROWS):
        y=row*Rect_height
        pygame.draw.line(window,Outline_Color,(0,y),(WIDTH,y),Outline_Thickness)
    for col in range(1,COLS):
        x=col*Rect_width
        pygame.draw.line(window,Outline_Color,(x,0),(x,HEIGHT),Outline_Thickness)
    pygame.draw.rect(window,Outline_Color,(0,0,WIDTH,HEIGHT),Outline_Thickness)
def draw(window):
    window.fill(Background_Color)
    drawGrid(window)
    pygame.display.update()
def main(window):
    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        draw(window)
    pygame.quit()    
if __name__=="__main__":
    main(window)