import pygame as pg
import random
from Functions import *
from Settings import *
from Classes import *
import time
from indices import *


################################################################################

class Team_Selector:
    def __init__(self):
        #Inicializacion
        pg.init()
        pg.mixer.init()

        #Cargar elementos
        self.load_data()

        #Variables
        self.nextpen=False
        self.shooted=False
        self.shootingpens=False
        self.now_shooting=False
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
        self.font_name= pg.font.match_font(FONT_NAME)
        pg.display.set_caption(TITLE)

    def new(self):

        #Grupos
        self.all_players= pg.sprite.Group()
        self.all_keepers= pg.sprite.Group()
        self.balls= pg.sprite.Group()
        self.all_sprites= pg.sprite.Group()
        self.all_images= pg.sprite.Group()
        self.selection_sprites= pg.sprite.Group()

        #Seleccionador
        self.selector= Image(self, 350,350,"Escudos")
        self.selection_sprites.add(self.selector)
        self.all_sprites.add(self.selector)


        self.run()

    def load_data(self):
        self.text_list=["Select a team!","Select 3 players!",
        "Select your keeper!","You can't choose the same player two times!","These are your players!","Press Space to confirm!"]
        self.text_ind=0

        self.timer_text=0
        self.pens_text="Shooting!"
        self.goal_text=""

    def run(self):
        #Loop del juego
        self.playing= True
        while self.playing:
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
            if self.text_ind!=4:
                self.text_ind=4
            else:
                pass

    def events(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()

        if self.shootingpens:
            self.shoot=True
            print(" No Waiting")
            if self.shoot:
                if now-self.timer>1000:
                    if self.timer_text<5:
                        self.timer=now
                        self.timer_text+=1
                        self.pens_text="Preparing!"
                    elif self.pens_text=="Preparing!":
                        self.pens_text="Shooting!"
                    else:
                        if now-self.timer>4000 and not self.now_shooting:
                            self.goal_text="Failed!"
                            self.shootingpens=False
                            self.nextpen=True


                        elif keys[pg.K_0] and not self.shooted:
                            self.shooted=True
                            self.now_shooting=True
                            self.timer=now
                            if atajar(0) :
                                self.goal_text="Goal!"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Goal")

                            else:
                                self.goal_text="Failed"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Failed")

                        elif keys[pg.K_1] and not self.shooted:
                            self.shooted=True
                            self.now_shooting=True
                            self.timer=now
                            if atajar(1) :
                                self.goal_text="Goal!"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Goal")

                            else:
                                self.goal_text="Failed"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Failed")

                        elif keys[pg.K_2] and not self.shooted:
                            self.shooted=True
                            self.now_shooting=True
                            self.timer=now
                            if atajar(2) :
                                self.goal_text="Goal!"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Goal")

                            else:
                                self.goal_text="Failed"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Failed")

                        elif keys[pg.K_3] and not self.shooted:
                            self.shooted=True
                            self.now_shooting=True
                            self.timer=now
                            if atajar(3) :
                                self.goal_text="Goal!"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Goal")

                            else:
                                self.goal_text="Failed"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Failed")

                        elif keys[pg.K_4] and not self.shooted:
                            self.shooted=True
                            self.now_shooting=True
                            self.timer=now
                            if atajar(4) :
                                self.goal_text="Goal!"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Goal")

                            else:
                                self.goal_text="Failed"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Failed")

                        elif keys[pg.K_5] and not self.shooted:
                            self.shooted=True
                            self.now_shooting=True
                            self.timer=now
                            if atajar(5) :
                                self.goal_text="Goal!"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Goal")

                            else:
                                self.goal_text="Failed"
                                self.shootingpens=False
                                self.nextpen=True
                                print("Failed")



        elif self.nextpen:
            print("Waiting")
            self.pens_text="Waiting for next penalty!"
            if keys[pg.K_SPACE]:
                self.shootingpens=True
                self.nextpen=False
                self.timer_text=0
                self.timer=now
                self.now_shooting=False
                self.shooted=False
                self.goal_text=""



        #Seleccion
        elif self.selecting and not self.showing:
            if keys[pg.K_RIGHT] and now-self.timer>250:
                self.timer=now
                self.selector.animate_right()

            if keys[pg.K_LEFT] and now-self.timer>250:
                self.timer=now
                self.selector.animate_left()

            if keys[pg.K_SPACE] and now- self.timer>250:
                self.timer= now
                self.selector.selection()

        elif self.selector.selecting_keeper and not self.showing:
            if keys[pg.K_SPACE]:
                self.selector.select_keeper()

        elif self.showing:
            if keys[pg.K_SPACE] and not self.selector.selecting_keeper:
                self.timer=now
                self.selector.selecting_keeper=True

            elif keys[pg.K_SPACE] and now-self.timer>250:
                self.timer=now
                self.running=False
                self.playing=False

    def draw(self):
        self.screen.fill(BGCOLOR)

        if self.shootingpens or self.nextpen:

            self.draw_text(str(self.timer_text),40,WHITE,350,10)
            self.draw_text(str(self.pens_text),40,WHITE,350,60)
            self.draw_text(str(self.goal_text),40,WHITE,350,110)

            pg.display.flip()


        elif self.selector.selecting_keeper and not self.showing:
            self.draw_text(self.text_list[2],40,WHITE,350,10)
            self.draw_text(Keeper_Names[self.selector.fil][self.selector.col],40,WHITE,350,60)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()


        elif self.selecting_player and not self.showing:
            self.draw_text(self.text_list[self.text_ind],40,WHITE,350,10)
            self.draw_text(Player_Names[self.selector.fil][self.selector.col],40,WHITE,350,60)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()

        elif self.showing:
            self.draw_text("Press Space to advance!",40,WHITE,350,10)
            self.draw_text(self.header,40,WHITE,350,60)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()

        else:
            self.draw_text(self.header,40,WHITE,350,10)
            self.draw_text(Team_Names[self.selector.ind],40,WHITE,350,60)
            self.selection_sprites.draw(self.screen)
            pg.display.flip()

    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            font= pg.font.Font(self.font_name, size)
            text_surface= font.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)


class Referee_Selector:
    def __init__(self):
        #Inicializacion
        pg.init()
        pg.mixer.init()

        #Cargar elementos
        self.load_data()

        #Funcionamiento
        self.running=True
        self.clock= pg.time.Clock()
        self.screen= pg.display.set_mode((WIDTH,HEIGHT))
        self.font_name= pg.font.match_font(FONT_NAME)
        pg.display.set_caption(TITLE)



    def new(self):

        #Grupos
        self.all_sprites= pg.sprite.Group()


        #Inicializacion del nuevo juego
        self.run()

    def load_data(self):
        pass

    def run(self):
        self.playing=True

        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            self.update()
            for event in pg.event.get(): #Cierra juego
                if event.type == pg.QUIT:
                    pg.quit()

    def update(self):
        pass
    def events(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()

        if keys[pg.K_SPACE]:
            self.running=False
            self.playing=False



    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_text("ESTO ES UNA PRUEBA",40,WHITE,350,350)


        pg.display.flip()

    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            font= pg.font.Font(self.font_name, size)
            text_surface= font.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)



################################################################################

Team1=[]
Selected1=[]
Portero1=[]

Team2=[]
Selected2=[]
Portero2=[]

Arbitros=[]

Ref=Referee_Selector()

while Ref.running:
    Ref.new()


G= Team_Selector()

while G.running:
    G.new()

Team1=G.selector.team1
Selected1=G.selector.selected1
Portero1=G.selector.keepers1


H= Team_Selector()

while H.running:
    H.new()

Team2=H.selector.team1
Selected2=H.selector.selected1
Portero2=H.selector.keepers1
