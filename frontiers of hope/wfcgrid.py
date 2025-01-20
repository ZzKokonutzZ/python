# import pygame as pg
# import sys
from random import randint,choices


class Tile() :
    def __init__(self,coords,max_coords,tiles):
        """create a tile that holds its possible states

        Args:
            coords : tuple of int, coordinates of the tile
            max_coords : tuple of int, max coordinates of the grid
            tiles : list of possible states
        """
        #int coordinates of the tile
        self.x,self.y=coords
        
        #create the list of the keys to the adjacent tiles
        self.adjacent_tiles={}
        if 0 <= self.x-1  :
            self.adjacent_tiles["left"] = (self.x-1,self.y)
        if self.x+1 < max_coords[0] :
            self.adjacent_tiles["right"] = (self.x+1,self.y)
        
        if 0 <= self.y-1  :
            self.adjacent_tiles["down"] = (self.x,self.y-1)
        if self.y+1<max_coords[1] :
            self.adjacent_tiles["up"] = (self.x,self.y+1)
        
        self.tiles = [e for e in tiles]
        self.buffer = [e for e in tiles]
        self.uncertainty = len(tiles)
        self.collapsed = False
    
    # sets the tile list to the buffer
    def update(self) :
        holder = [e for e in self.buffer]
        self.tiles = holder

class Grid() :
    def __init__(self,x=10,y=10,tiles_indexes=[],dependencies={"up":{},"down":{},"right":{},"left":{}},distribution={}):
        """create a grid of tiles with built-in functions for wave function collapse

        Args:
            x : int, length of the grid. Defaults to 10.
            y : int, width of the grid. Defaults to 10.
            tiles_indexes : list, list of indexes to the elements you use as tiles. Defaults to [].
            dependencies : dict of 4 dict with keys "up","down","right","left", each subdict contains which tile can be next to a given tile key. Defaults to {"up":{},"down":{},"right":{},"left":{}}.
        
        Attributes :
            xmax, ymax : max index of the grid
            grid : actual grid of tiles indexed by a tuple of int for x and y coordinates
            keys : list of grid keys
            dependencies : dependencies dict given in argument
            tile_set : list of indexes to objects used as tiles
            unstable_keys : keys of tiles that aren't collapsed

        """
        self.xmax = x
        self.ymax = y
        
        self.grid = {}
        self.keys = []

        self.dependencies = dependencies
        self.tile_set = tiles_indexes
                
        for i in range(x) :
            for j in range(y) :
                self.grid[(i,j)] = Tile((i,j),(x,y),tiles_indexes)
                self.keys.append((i,j))
        
        self.unstable_keys = [e for e in self.grid]
        self.distribution={}
        if distribution=={} :
            for e in tiles_indexes :
                self.distribution[e]=1
        else :
            self.distribution=distribution
    
    ####### sort unstable_keys by uncertainty and removes collapsed tiles ########
    def update_uncertainty(self) :
        for e in self.unstable_keys :
            self.grid[e].uncertainty = len(self.grid[e].tiles)
        self.unstable_keys.sort(key=lambda x : self.grid[x].uncertainty)
        
        while len(self.unstable_keys) > 0 and self.grid[self.unstable_keys[0]] == 1 :
            self.unstable_keys.pop(0)
    
    ########## sets the grid back to it's initial state #############
    def reset_grid(self):
        self.grid = {}
        self.keys = []
        for i in range(self.xmax) :
            for j in range(self.ymax) :
                self.grid[(i,j)] = Tile((i,j),(self.xmax,self.ymax),self.tile_set)
                self.keys.append((i,j))

        self.unstable_keys = []
        for e in self.grid :
            self.unstable_keys.append(e)
        self.update_uncertainty()
            
    ####### removes every tile not matching with coords_elements from coords_a buffer 
    def compare(self, coords_a,pos,coords_b) :
        
        trash=[]
        
        if self.grid[coords_b].collapsed :        
            for e in self.grid[coords_a].buffer :
                if not(self.grid[coords_b].tiles[0] in self.dependencies[pos][e]) :
                    trash.append(e)
        else :
            for e in self.grid[coords_a].buffer :
                relation = False
                for ref in self.grid[coords_b].tiles :
                    if ref in self.dependencies[pos][e] :
                        relation = True
                        break
                if not relation :
                    trash.append(e)
                    
        for e in trash :
            self.grid[coords_a].buffer.remove(e)
            if len(self.grid[coords_a].buffer) <= 0 :
                return "error : no tile can fit in this spot"

    ########## removes every non matching tiles from this tile's buffer ##################
    def reduce(self,coords) :
        check_pos = self.grid[coords].adjacent_tiles
        for pos in check_pos :
            catch = self.compare(coords,pos,check_pos[pos])
            if catch != None :
                return catch
    
    ########## collapse one tile : set the tile at coords to a random element of its possible tiles #############
    def tile_collapse(self,coords) :
        self.grid[coords].tiles = choices(self.grid[coords].tiles,weights=[self.distribution[e] for e in self.grid[coords].tiles])
        self.grid[coords].collapsed = True
    
    ############### collapse the grid : removes every non-matching tile and collapse one of the tiles with the lowest uncertainty ###########################
    def grid_collapse(self) :
        for e in self.unstable_keys :
            if not(self.grid[e].collapsed) :
                check = self.reduce(e)
                if check != None :
                    print(check)
                    return "unsolvable tile pattern happened"
        
        for e in self.unstable_keys :
            self.grid[e].update()
            
        tile = self.unstable_keys.pop(0)
        self.tile_collapse(tile)
        
        self.update_uncertainty()
    
    ############ collapse the grid until it finds a fully solved arrangement #################
    def global_collapse(self) :
        
        check=None
        
        while len(self.unstable_keys)>0 :
            
            check = self.grid_collapse()
            
            if check != None :
                print(check)
                self.reset_grid()
        
        self.clean()
                
    ############ set the tile at coords to the element e #######################
    def assign(self,coords,e) :
        
        self.grid[coords].tiles = [e]
        self.grid[coords].buffer = [e]
        
        self.grid[coords].collapsed = True
        
        self.update_uncertainty()
    
    ########### change all the list tile to its single element #########
    def clean(self) :
        for e in self.keys :
            self.grid[e].tiles = self.grid[e].tiles[0]


###################################### examples #########################################################################################

# pg.init()
# screen=pg.display.set_mode((500,500))


# colors=[(213,62,79),(244,109,67),(253,174,97),(254,224,139),(230,245,152),(171,221,164),(102,194,165),(50,136,189)]

# dependencies={"up":{},"down":{},"right":{},"left":{}}
# keys=["up","down","right","left"]

# for e in keys:
#     dependencies[e][0]=[0,1]
#     dependencies[e][7]=[6,7]
#     for i in range(1,7) :
#         dependencies[e][i]=[i-1,i,i+1]
        
# side=50

# tilemap=Grid(side,side,[0,1,2,3,4,5,6,7],dependencies)

# tilemap.assign((side//2,side//2),3)

# pix=500//side

# ##### example 1 : showing the resolving process #####
# def example1() :
#     while 1 :
#         screen.fill((0,0,0))
#         for i in range(tilemap.xmax) :
#             for j in range(tilemap.ymax) :
#                 if tilemap.grid[(i,j)].collapsed :
#                     pg.draw.rect(screen,colors[tilemap.grid[(i,j)].tiles[0]],(pix*i,pix*j,pix,pix))
#                 else :
#                     pg.draw.rect(screen,colors[tilemap.grid[(i,j)].tiles[0]],(pix*i,pix*j,pix,pix))
#         pg.display.flip()
#         if len(tilemap.unstable_keys)>0 :
#             check=tilemap.grid_collapse()
#             if check!=None :
#                 print(check)
#                 tilemap.reset_grid()
#         for event in pg.event.get() :
#             if event.type==pg.QUIT :
#                 pg.quit()
#                 sys.exit()

# ##### example 2 : resolving the grid before showing #####

# def example2() :
    
#     tilemap.global_collapse()
    
#     while 1 :
#         screen.fill((0,0,0))
#         for e in tilemap.keys :
#             pg.draw.rect(screen,colors[tilemap.grid[e].tiles],(pix*e[0],pix*e[1],pix,pix))
#         pg.display.flip()
#         for event in pg.event.get() :
#             if event.type==pg.QUIT :
#                 pg.quit()
#                 sys.exit()

# ########################################################################################################################
# example1()