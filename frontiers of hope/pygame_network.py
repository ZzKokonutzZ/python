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
    msg=pickle.dumps(msg)
    header=str(len(msg)).encode(FORMAT)+b' '*(HEADER-len(str(len(msg)).encode(FORMAT)))
    channel.send(header)
    channel.send(msg)

def recieve(channel):
    size = int(channel.recv(HEADER).decode(FORMAT).strip())
    data = b""
    while len(data) < size:
        packet = channel.recv(size - len(data)).strip()
        if not packet:
            break
        data += packet
    if len(data)>0 :
        msg = pickle.loads(data)
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
        self.sprites=[]
        self.new_players_buffer=0
    
    def create_object(self,sprite,coords) :
        self.sprites.append([sprite,coords])
        return self.sprites[-1]
            
    
    class player() :
        def __init__(self) :
            self.keys=[]
            self.keys_buffer=[]
            
    def run_main(self):
        pass
    
    def keys_update(self,n) :
        self.players[n].keys=self.players[n].keys_buffer[:]
    
    def accept_new_players(self):
        self.new_players_buffer=1
        
    def stop_updates(self) :
        self.new_players_buffer=0
    
    def new_player_setup(self,n) :
        pass
    
    def run(self) :
        def update_player(n,channel) :
            while not self.new_players_buffer :
                pass
            connected=1
            self.players[n]=self.player()
            send(n,channel)
            print("player rank sent")
            self.nb_players+=1
            self.new_player_setup(self,n)
            while connected :
                run=int(recieve(channel))
                if run :
                    self.players[n].keys_buffer=recieve(channel)
                    #for i in range(len(self.sprites)) :
                        #print(self.sprites[i])
                    send(self.sprites,channel)
                else :
                    connected=0
                    del self.players[n]
                    self.nb_players-=1
        
        def connection_update() :
            n=0
            while 1 :
                channel,ip=self.main.accept()
                print(f"new connection : {ip}")
                threading.Thread(target=update_player,args=(n,channel)).start()
                n+=1
        threading.Thread(target=connection_update).start()
        
        self.run_main(self)


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
            send(keys,self.main)
            sprites=recieve(self.main)
            self.screen.fill((0,0,0))
            for i in range(len(sprites)) :
                self.screen.blit(self.sprites_memory[sprites[i][0]],tuple(sprites[i][1]))
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
            
            