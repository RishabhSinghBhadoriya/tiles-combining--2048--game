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
class Tile:
    COLORS=[
        (237,229,218),
        (238,225,201),
        (243,178,122),
        (246,150,101),
        (247,124,95),
        (247,95,59),
        (237,208,115),
        (237,204,99),
        (236,202,80),
    ]
    def __init__(self,value,row,col):
        self.value=value
        self.row=row
        self.col=col
        self.x=col*Rect_width
        self.y=col*Rect_height
    def get_color(self):
        #get color as per the color defined above
        #so basically get color value as per the values like for 2 the color would the zero indexed color
        #f(2)=0
        #f(4)=1
        color_index=int(math.log2(self.value))-1
        color=self.COLORS[color_index]
        return color
    def draw(self,window):
        color=self.get_color()
        pygame.draw.rect(window,color,(self.x,self.y,Rect_width,Rect_height))
        text=FONT.render(str(self.value),1,Font_Color)
        #to make text appear at the centre of tile
        window.blit(text,(self.x+(Rect_width/2-text.get_width()/2),self.y+(Rect_height/2-text.get_height()/2)))
    def set_pos(self):
        pass
    def move(self,delta):
        pass   
        
def drawGrid(window):
    for row in range(1,ROWS):
        y=row*Rect_height
        pygame.draw.line(window,Outline_Color,(0,y),(WIDTH,y),Outline_Thickness)
    for col in range(1,COLS):
        x=col*Rect_width
        pygame.draw.line(window,Outline_Color,(x,0),(x,HEIGHT),Outline_Thickness)
    pygame.draw.rect(window,Outline_Color,(0,0,WIDTH,HEIGHT),Outline_Thickness)
def draw(window,tiles):
    window.fill(Background_Color)
    for tile in tiles.values():
        tile.draw(window)
    drawGrid(window)
    pygame.display.update()
def main(window):
    clock=pygame.time.Clock()
    run=True
    tiles={"00":Tile(4,0,0),"20":Tile(128,2,0),"02":Tile(64,0,2)}
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                break
        draw(window,tiles)
    pygame.quit()    
if __name__=="__main__":
    main(window)