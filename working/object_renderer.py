import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_texture = self.load_wall_texture()


    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        #The load function returns a Surface object, which is Pygame's term for an image loaded into memory that can be drawn on the screen.
        #convert_alpha method converts the Surface to a pixel format that includes per-pixel alpha. Alpha is a measure of transparency, 
        # and per-pixel alpha means that each pixel in the image can have its own level of transparency
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
    
    def load_wall_texture(self):
        return {
            1 : self.get_texture('resources/textures/1.png'),
            2 : self.get_texture('resources/textures/2.png'),
            3 : self.get_texture('resources/textures/3.png'),
            4 : self.get_texture('resources/textures/4.png'),
            5 : self.get_texture('resources/textures/5.png'),
        }
