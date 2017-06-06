import pygame as pg
import random
from Functions import *
from Settings import *
from Classes import *
import time





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Game:
    def __init__(self):
        #Inicializacion
        pg.init()
        pg.mixer.init()

        #Variables
        self.waiting=False
        self.selecting=False
        self.selecting_player=False
        self.running=True
        self.showing=False
        self.timer=0
        self.selection=0

        #Listas
        self.selected=[]

        #Funcionamiento
        self.clock= pg.time.Clock()
        self.screen= pg.display.set_mode((WIDTH,HEIGHT))
        self.font_name= pg.font.match_font(FONT_NAME)
        pg.display.set_caption(TITLE)

        #Cargar elementos
        self.load_data()


    def load_data(self):
        #Logos
        Logos=LOGOS
        Logosheet= Spritesheet(Logos)
        self.images_list=[Logosheet.get_image(0,0,587,647), Logosheet.get_image(582,0,1076,646),
        Logosheet.get_image(1085,0,1759,646)]
        for image in self.images_list:
            image.set_colorkey(BLACK)

        #Jugadores

        #Porteros


    def new(self):




    def run(self):


    def update(self):
        self.all_sprites.update()


    def events(self):






"""
        if self.waiting:
            if keys[pg.K_p]:
                self.waiting=False
                self.show_selection()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

    def show_menu(self):
        self.screen.fill(BGCOLOR)
        self.draw_text("Press P to play!", 40, WHITE, WIDTH/2, HEIGHT/2)
        pg.display.flip()
        self.wait_for_key()

    def show_selection(self):
        self.selecting= True
        self.screen.fill(BGCOLOR)
        self.screen.blit(self.images_list[self.selection],(0,0))
        self.clock.tick(FPS)
        self.events()
        self.update()
        pg.display.flip()





    def select_player(self):
        self.selecting=False
        self.selecting_player=True
        self.screen.fill(BGCOLOR)
        self.draw_text("Aqui van los jugadores",40,WHITE,350,350)
        pg.display.flip()




    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            font= pg.font.Font(self.font_name, size)
            text_surface= font.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)


    def wait_for_key(self): #Funcion que espera el evento de presionar una tecla
            self.waiting=True
            keys= pg.key.get_pressed()
            now= pg.time.get_ticks()
            while self.waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type== pg.QUIT:
                        self.waiting= False
                        pg.quit()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_p:
                            self.show_selection()
                            self.waiting=False
                            print("ok")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
g=Game()

g.show_menu()

while g.running:
    g.new()
