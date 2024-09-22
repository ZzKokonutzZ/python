import pygame_network as pgn
server=pgn.Server()
channel,ip=server.main.accept()
print(f"new connection : {ip}")
while 1 :
    pgn.send("ping",channel)
    print(pgn.recieve(channel))