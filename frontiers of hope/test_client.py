import pygame_network as pgn
import pygame as pg
pg.init()
client=pgn.Client()
client.sprites_memory["square"]=pg.image.load("pixel.png")
print('memory updated')
client.run()