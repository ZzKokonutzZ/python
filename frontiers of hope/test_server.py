import pygame_network as pgn
import numpy as np
server=pgn.Server()

server.players_sprites={}
def new_circle() :
    circle=[]
    for i in range(100):
        circle.append([250+100*np.cos(i),250+100*np.sin(i)])
    return circle

def new_player_setup(self,n) :
    holder=new_circle()
    self.players_sprites[n]=[]
    for i in range(len(holder)) :
        self.players_sprites[n].append(self.create_object("s",holder[i]))


    
def run_main(self) :
    t=0
    while 1 :
        server.stop_updates()
        for n in self.players :
            server.keys_update(n)
            for i in range(len(self.players[n].keys)) :
                k=self.players[n].keys[i]
                if k=='right' :
                    t+=0.1
                if k=='left' :
                    t-=0.1
            
                for i in range(len(self.players_sprites[n])) :
                    assert len(self.players_sprites[n][i])==2, self.players_sprites[n][i]
                    self.players_sprites[n][i][1][0]=100*np.cos(i+t)+250
                    self.players_sprites[n][i][1][1]=100*np.sin(i+t)+250
        server.accept_new_players()

server.new_player_setup=new_player_setup
server.run_main=run_main
server.run()