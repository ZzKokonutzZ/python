import socket
import pickle
import pygame as pg
import threading
import sys
pg.init()
CLOCK=pg.time.Clock()
HEADER=4096
FORMAT="utf-8"


def send(msg,channel) :
    # print("[SENDING]",end='')
    # print(msg)
    msg=pickle.dumps(msg)
    header=str(len(msg)).encode(FORMAT)+b' '*(HEADER-len(str(len(msg)).encode(FORMAT)))
    channel.send(header)
    channel.send(msg)

def recieve(channel) :
    # print("[RECIEVING]",end='')
    size=int(channel.recv(HEADER).decode(FORMAT))
    msg=channel.recv(size)
    msg=pickle.loads(msg)
    # print(msg)
    return msg


class Server() :
    def __init__(self) :
        self.PORT=5050
        self.SERVER_IP=socket.gethostbyname(socket.gethostname())
        self.main=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ADDR=(self.SERVER_IP,self.PORT)
        self.main.bind(ADDR)
        self.main.listen()
        print(f"server opened with address {self.SERVER_IP}")
        self.players={}
        self.nb_players=0
        self.sprites={}
        self.sprites_player=[]
        self.sprites_coords={}
        self.sprites_player_coords=[]
        self.k_update=0
        
    class player() :
        def __init__(self) :
            self.keys=[]
            
    def game_loop(self) :
        pass
    
    def define_variables(self) :
        pass
    
        
    def run(self) :
        def update_player(n,channel) :
            connected=1
            self.players[n]=self.player()
            self.sprites[n]=self.sprites_player
            self.sprites_coords[n]=self.sprites_player_coords
            # print(self.sprites)
            send(n,channel)
            print("player rank sent")
            while connected :
                run=int(recieve(channel))
                if run :
                    keys=recieve(channel)
                    for e in "['] ":
                        keys=keys.replace(e,'')
                    keys=keys.split(',')
                    while not self.k_update :
                        pass
                    self.players[n].keys=keys
                    send(str(self.sprites[n]).replace(' ',''),channel)
                    send(str(self.sprites_coords[n]).replace(' ',''),channel)
                else :
                    connected=0
                    del self.players[n]
        
        def connection_update() :
            n=0
            while 1 :
                channel,ip=self.main.accept()
                print(f"new connection : {ip}")
                threading.Thread(target=update_player,args=(n,channel)).start()
                n+=1
        threading.Thread(target=connection_update).start()
        
        while 1 :
            self.k_update=0
            self.game_loop(self)
            self.k_update=1
            CLOCK.tick(60)

class Client() :
    def __init__(self) :
        self.PORT=5050
        self.SERVER_IP=input()
        self.main=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ADDR=(self.SERVER_IP,self.PORT)
        self.main.connect(self.ADDR)
        print('connected')
        self.screen=pg.display.set_mode((500,500))
        self.sprites_memory={}
    
    def run(self) :
        running=1
        keys=[]
        p_n=int(recieve(self.main))
        print("player rank recieved")
        send(1,self.main)
        print("setup done")
        while running :
            send(str(keys).replace(' ',''),self.main)
            sprites=recieve(self.main).replace('[','')
            coords=recieve(self.main).replace('[','')
            
            for e in "[']" :
                sprites=sprites.replace(e,'')
                coords=coords.replace(e,'')
            
            sprites=sprites.split(',')
            coords=coords.split(',')
            for i in range(len(coords)) :
                coords[i]=float(coords[i])
            self.screen.fill((0,0,0))
            i=0
            for e in sprites :
                self.screen.blit(self.sprites_memory[e],(coords[i],coords[i+1]))
                i+=2
            pg.display.flip()
            
            events=pg.event.get()
            for event in events :
                if event.type==pg.KEYDOWN :
                    # print(event.key)
                    if event.key==pg.K_ESCAPE :
                        running=0
                        send(running,self.main)
                        pg.quit()
                        sys.exit()
                    elif pg.key.name(event.key) not in keys :
                        keys+=[pg.key.name(event.key)]
                        # print(keys)
                        
                if event.type==pg.KEYUP :
                    if pg.key.name(event.key) in keys :
                        keys.remove(pg.key.name(event.key))
                        # print('keys remove')
                        
                if event.type==pg.QUIT :
                    running=0
                    send(running,self.main)
                    pg.quit()
                    sys.exit()
                
            send(running,self.main)
            
            