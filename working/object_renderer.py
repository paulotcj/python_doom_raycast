import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_texture()
        self.sky_image = self.get_texture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = ( self.sky_offset + 4.0 * self.game.player.rel ) % WIDTH
        self.screen.blit( self.sky_image, (-self.sky_offset, 0) )
        self.screen.blit( self.sky_image, (-self.sky_offset + WIDTH, 0) )
        #floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.ray_casting.objects_to_render

        for depth, image, pos in list_objects:
            self.screen.blit(image,pos)


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
