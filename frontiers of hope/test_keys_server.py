import pygame_network as pgn
import pygame as pg
pg.init()
server=pgn.Server()
channel,ip=server.main.accept()
print(f"new connection : {ip}")
screen=pg.display.set_mode((500,500))
held_keys=[]
while 1 :
    for event in pg.event.get():
        if event.type==pg.KEYDOWN :
            held_keys.append(pg.key.name(event.key))
        if event.type==pg.KEYUP :
            held_keys.remove(pg.key.name(event.key))
    for e in held_keys :
        pgn.send(e,channel)
        print(pgn.recieve(channel))
    