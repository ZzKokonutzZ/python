import pygame_network as pgn
client=pgn.Client()
while 1 :
    print(pgn.recieve(client.main))
    pgn.send("pong",client.main)