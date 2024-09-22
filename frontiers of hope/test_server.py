import pygame_network as pgn
import pygame as pg
pg.init()
server=pgn.Server()

server.sprites_for_player=["square",[0,0]]
def game_loop(self) :
    for n in self.players :
        for i in range(len(self.players[n].keys)) :
            
            k=self.players[n].keys[i]
            if k==pg.K_RIGHT :
                self.sprites[n][0][1][0]+=3
            if k==pg.K_LEFT :
                self.sprites[n][0][1][0]-=3
                
            if k==pg.K_UP :
                self.sprites[n][0][1][1]-=3
            if k==pg.K_DOWN :
                self.sprites[n][0][1][1]+=3
server.game_loop=game_loop
server.run()