import pygame_network as pgn
import pygame as pg
pg.init()
client=pgn.Client()
client.sprites_memory["s"]=pg.image.load("pixel.png")
client.run()