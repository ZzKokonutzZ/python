import pygame_network as pgn
import numpy as np
server=pgn.Server()

server.sprites_player=[]
server.sprites_player_coords=[]
for i in range(100):
    server.sprites_player.append("s")
    server.sprites_player_coords+=[100*np.cos(i),100*np.sin(i)]

server.t=0
    
def game_loop(self) :
    for n in self.players :
        for i in range(len(self.players[n].keys)) :
            
            k=self.players[n].keys[i]
            if k=='right' :
                self.t+=0.1
            if k=='left' :
                self.t-=0.1
            
            for i in range(len(self.sprites_coords[n])//2) :
                self.sprites_coords[n][2*i]=100*np.cos(i+self.t)+250
                self.sprites_coords[n][2*i+1]=100*np.sin(i+self.t)+250

server.game_loop=game_loop
server.run()