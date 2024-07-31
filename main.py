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
        #so basically get color value as per the values like for 2 the color would the zero indexed color and so  on
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
        self.x+=delta[0]
        self.y+=delta[1]   
        
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

def get_random_pos(tiles):
    row=None
    col=None
    while True:
        row=random.randrange(0,ROWS)
        col=random.randrange(0,COLS)
        if f"{row}{col}" not in tiles:
            break
    return row,col
def move_tiles(window,tiles,clock,direction):
    updated=True
    blocks=set()
    if direction=="left":
        sort=lambda x:x.col
        reverse=False
        delta=(-MOV_VEL,0)
        boundary=lambda tile:tile.col==0
        getnext=lambda tile:tiles.get(f"{tile.row}{tile.col-1}")
        mergecheck=lambda tile,next_tile:tile.x>next_tile.x+MOV_VEL                 #to check are we in the position for merging can the tiles be merged
        movecheck=lambda tile,next_tile:tile.x>next_tile.x+Rect_width+MOV_VEL

    elif direction=="right":
        pass
    elif direction=="up":
        pass
    elif direction=="down":
        pass
    while updated:
        clock.tick(FPS)
        updated=False
        sortedtiles=sorted(tiles.values(),key=sort,reverse=reverse)
        for i,tile in enumerate(sortedtiles):
            if boundary(tile):
                continue
            next_tile=getnext(tile)
            if not next_tile:
                tile.move(delta)
            elif tile.value==next_tile.value and tile not in blocks and next_tile not in blocks:   #if the tile value are same then perform the below which is merge the tiles
                if mergecheck(tile,next_tile):
                    tile.move(delta)
                else:
                    next_tile.value*=2
                    sortedtiles.pop(i)
                    blocks.add(next_tile)
def generateTiles():
    tiles={}
    for _ in range(2):
        row,col=get_random_pos(tiles)
        tiles[f"{row}{col}"]=Tile(2,row,col)
    return tiles

def main(window):
    clock=pygame.time.Clock()
    run=True
    tiles=generateTiles()
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