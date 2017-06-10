import pygame as pg
import random
from Seleccion.Classes import *
import time

################################################################################

class Game:
    def __init__(self):
        #Inicializacion
        pg.init()
        pg.mixer.init()

        #Cargar elementos
        self.load_data()

        #Variables
        self.Selecting_referee = False
        self.finish = False
        self.waiting=False
        self.selecting=True
        self.selecting_player=False
        self.showing=False
        self.running=True
        self.timer=0
        self.selection=0
        self.header=self.text_list[self.text_ind]
        #Listas
        self.selected=[]

        #Funcionamiento
        self.clock= pg.time.Clock()
        self.screen= pg.display.set_mode((WIDTH,HEIGHT))
        self.Medium_text= pg.font.Font('Fonts/Exo-Medium.otf', 26)
        pg.display.set_caption(TITLE)



    def new(self):
        self.__init__()
        #Grupos
        self.all_players= pg.sprite.Group()
        self.all_keepers= pg.sprite.Group()
        self.balls= pg.sprite.Group()
        self.all_sprites= pg.sprite.Group()
        self.all_images= pg.sprite.Group()
        self.selection_sprites= pg.sprite.Group()

        #Seleccionador
        self.selector= Image(self, WIDTH//2,HEIGHT//2 + 30,"Escudos")
        self.selection_sprites.add(self.selector)
        self.all_sprites.add(self.selector)


        self.run()

    def load_data(self):
        self.text_list=["Select a team!","Select 3 players!",
        "Select your keeper!","You can't choose the same player two times!","These are your players!","Press Space to confirm!"]
        self.text_ind=0


    def run(self):
        #Loop del juego
        self.playing= True
        while self.playing:
            if self.selector.finished == True:
                self.playing = False
            self.selecting=True
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
            for event in pg.event.get(): #Cierra juego
                if event.type == pg.QUIT:
                    pg.quit()

    def update(self):
        if self.showing:
            self.selector.scroll()
            self.finish = True
            if self.text_ind!=4:
                self.text_ind=4
            else:
                pass

    def events(self):
        keys = pg.key.get_pressed()
        now = pg.time.get_ticks()

        if self.selecting and not self.showing:
            if keys[pg.K_RIGHT] and now - self.timer > 250:
                self.timer = now
                self.selector.animate_right()

            if keys[pg.K_LEFT] and now - self.timer > 250:
                self.timer = now
                self.selector.animate_left()

            if keys[pg.K_SPACE] and now - self.timer > 250:
                self.timer = now

                self.selector.selection()


        elif self.selector.selecting_keeper and not self.showing:
            if keys[pg.K_SPACE]:
                self.selector.select_keeper()

        elif self.showing:
            if keys[pg.K_SPACE] and not self.selector.selecting_keeper:
                self.timer = now
                self.selector.selecting_keeper = True


    def draw(self):
        self.screen.blit(pg.image.load(Background_img), (0, 0))

        if self.selector.selecting_keeper and not self.showing:
            self.draw_text(self.text_list[2], 40, WHITE, WIDTH//2, 10)
            self.draw_text(Keeper_Names[self.selector.fil][self.selector.col], 40, WHITE, WIDTH//2, 50)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()


        elif self.selecting_player and not self.showing:
            self.draw_text(self.text_list[self.text_ind], 40, WHITE, WIDTH//2, 10)
            self.draw_text(Player_Names[self.selector.fil][self.selector.col], 40, WHITE, WIDTH//2, 50)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()
        elif self.showing:
            self.draw_text("Press Space to advance!", 40, WHITE, WIDTH//2, 10)
            self.draw_text(self.header, 40, WHITE, WIDTH//2, 50)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()
            self.finish = True

        else:
            self.draw_text(self.header, 40, WHITE, WIDTH//2, 10)
            self.draw_text(Team_Names[self.selector.ind], 40, WHITE, WIDTH//2, 50)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()


    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            text_surface= self.Medium_text.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)

#G= Game()

#while G.running:
 #   G.new()
