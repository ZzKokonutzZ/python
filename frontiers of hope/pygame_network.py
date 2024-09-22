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
    print("[SENDING]")
    print(msg)
    msg=pickle.dumps(msg)
    print(msg)
    header=str(len(msg)).encode(FORMAT)+b' '*(HEADER-len(str(len(msg)).encode(FORMAT)))
    print(msg)
    channel.send(header)
    print(msg)
    channel.send(msg)

def recieve(channel) :
    print("[RECIEVING]")
    size=int(channel.recv(HEADER).decode(FORMAT))
    msg=channel.recv(size)
    print(msg)
    msg=pickle.loads(msg)
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
        self.sprites_for_player=[]
        self.k_update=0
    class player() :
        def __init__(self) :
            self.keys=[]
    def game_loop(self) :
            pass
    def run(self) :
        def update_player(n,channel) :
            connected=1
            self.players[n]=self.player()
            self.sprites[n]=[]
            self.sprites[n].append(self.sprites_for_player)
            print(self.sprites)
            send(n,channel)
            print("player rank sent")
            while connected :
                run=int(recieve(channel))
                if run :
                    keys=recieve(channel)
                    while not self.k_update :
                        pass
                    self.players[n].keys=keys
                    send(self.sprites,channel)
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
            CLOCK.tick(30)

class Client() :
    def __init__(self) :
        self.PORT=5050
        self.SERVER_IP=input()
        self.main=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.ADDR=(self.SERVER_IP,self.PORT)
        self.main.connect(self.ADDR)
        print('connected')
        self.screen=pg.display.set_mode((1280,720),flags=pg.FULLSCREEN)
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
            for i in sprites :
                for j in range(len(sprites[i])) :
                    self.screen.blit(self.sprites_memory[sprites[i][j][0]],sprites[i][j][1])
            pg.display.flip()
            
            self.events=pg.event.get()
            for event in self.events :
                if event.type==pg.KEYDOWN :
                    print(event.key)
                    if event.key==pg.K_ESCAPE :
                        running=0
                        send(running,self.main)
                        pg.quit()
                        sys.exit()
                    elif event.key not in keys :
                        keys+=[event.key]
                        print(keys)
                    
                elif event.type==pg.QUIT :
                    running=0
                    send(running,self.main)
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYUP :
                    if event.key in keys :
                        keys.remove(event.key)
                        print('keys remove')
            send(running,self.main)
            
            