"Classes"
import pygame as pg
import random
from Functions import *
from Settings import *
vec= pg.math.Vector2




class Team:
    def __init__(self,Name, Players, Keepers):
        pg.sprite.Sprite.__init__(self)

        self.name= str(Name)
        self.players= Players
        self.keepers= Keepers
        self.playing= []  #range(0,7) #Una posicion del rango para cada jugador
        self.keeping= []  #range(0,3) #Una posicion del rango para cada portero
        self.banner= "" #Imagen del escudo

    def add_player(self, Num):
        if len(self.playing)<3:
            self.playing.append(self.players[Num])
        else:
            return "You have 3 players in your playing team!"

    def add_keeper(self, Num):
        if len(self.keeping)<1:
            self.keeping.append(self.keepers[Num])
        else:
            return "You already have a keeper!"


class Player:
    def __init__(self,Name, Number, Tag=""):
        pg.sprite.Sprite.__init__(self)

        self.name= str(Name)
        self.number= Number
        self.tag= Tag
        self.image= ""#Imagen del jugador
    #Assigned Ball
    #self.ball= Ball(x,y)

    def shoot_ball(self):
        #
        #
        #
        #
        #
        pass

class Ball:
    def __init__(self, x ,y):
        pg.sprite.Sprite.__init__(self)

        self.pos= vec(x,y)
        self.vel= vec(0,0)
        #self.dir=

class Keeper:
    def __init__(self, Name, Number, Tag=""):
        pg.sprite.Sprite.__init__(self)

        self.name= str(Name)
        self.number= Number
        self.tag= Tag
        self.image= "" #Imagen del jugador
        self.save_dir=0

    def catch_ball(self):
        self.save_dir= random.randrange(0,6)

class Image(pg.sprite.Sprite):
    def __init__(self, game, x, y, Team, fil=0, col=0):
        pg.sprite.Sprite.__init__(self)
        self.game=game
        Logos=LOGOS
        self.pos= vec(x,y)
        self.team= Team
        self.ind=0
        self.fil=0
        self.col= 0
        self.selecting_keeper= False
        self.load_images()
        self.image= self.images_list[self.ind]
        self.image.set_colorkey(RED)

        pg.transform.scale(self.image,(40,40))

        self.rect= self.image.get_rect()
        self.rect.center= vec(x,y)
        self.timer=0
        self.team=[]
        self.selected=[]
        self.keepers=[]

    def load_images(self):
        #Logos
        Logos=LOGOS
        Logosheet= Spritesheet(Logos)
        self.images_list=[Logosheet.get_image(2,0,418,413),
        Logosheet.get_image(451,0,418,413),
        Logosheet.get_image(1223,8,418,413)]
        for image in self.images_list:
            image.set_colorkey(RED)

        #Jugadores
        Real= REAL
        Realsheet= Spritesheet(Real)

        #Barcelona= BARCELONA
        #Bar_sheet= Spritesheet(Barcelona)

        #Bayern= BAYERN
        #Bayern_sheet= Spritesheet(Bayern)

        Keepers= KEEPERS
        Keeper_sheet= Spritesheet(Keepers)

                            #Barcelona
        self.player_images=[[],
                            #Real Madrid
                            [Realsheet.get_image(0,0,418,413),Realsheet.get_image(421,0,418,413),
                            Realsheet.get_image(876,0,418,413),Realsheet.get_image(1319,0,418,413),
                            Realsheet.get_image(1758,0,418,413),Realsheet.get_image(2176,0,418,413),
                            Realsheet.get_image(2597,0,418,413)],
                            #Bayern
                            []]
                            #Barcelona
        self.keeper_images=[[],
                            #Real Madrid
                            [Keeper_sheet.get_image(0,0,418,413),Keeper_sheet.get_image(431,0,418,413),
                            Keeper_sheet.get_image(1210,2,418,413)],
                            #Bayern
                            []]





        for image in self.player_images[1]:
            image.set_colorkey(COLORKEY)

        for image in self.keeper_images[1]:
            image.set_colorkey(COLORKEY)



    def animate_right(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()

        if self.selecting_keeper:
            if self.col == len(self.keeper_images[self.fil])-1:
                self.col=0
                self.image=self.keeper_images[self.fil][self.col]
                print(self.col)
            else:
                self.col+=1
                self.image=self.keeper_images[self.fil][self.col]

        elif self.game.selecting and not self.game.selecting_player:
            if self.ind == len(self.images_list)-1:
                self.ind=0
                self.image=self.images_list[self.ind]
                print(self.ind)
            else:
                self.ind+=1
                self.image=self.images_list[self.ind]

                print(self.ind)
        elif self.game.selecting_player:
            if self.col == len(self.player_images[self.fil])-1:
                self.col=0
                self.image=self.player_images[self.fil][self.col]
                print(self.col)
            else:
                self.col+=1
                self.image=self.player_images[self.fil][self.col]

    def animate_left(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()

        if self.selecting_keeper:
            if self.col == 0:
                self.col=len(self.keeper_images[self.fil])-1
                self.image=self.keeper_images[self.fil][self.col]
                print(self.col)
            else:
                self.col-=1
                self.image=self.keeper_images[self.fil][self.col]

        elif self.game.selecting and not self.game.selecting_player:
            if self.ind == 0:
                self.ind=len(self.images_list)-1
                self.image=self.images_list[self.ind]
                print(self.ind)
            else:
                self.ind-=1
                self.image=self.images_list[self.ind]

                print(self.ind)
        elif self.game.selecting_player:
            if self.col == 0:
                self.col=len(self.player_images[self.fil])-1
                self.image=self.player_images[self.fil][self.col]
                print(self.col)
            else:
                self.col-=1
                self.image=self.player_images[self.fil][self.col]

    def selection(self):

        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()

        if self.selecting_keeper:
            if len(self.keepers)<1:
                self.keepers.append(self.col)
            else:
                self.game.showing= True

        elif self.game.selecting and not self.game.selecting_player:

                if len(self.selected)<1:

                    self.selected.append(self.ind)
                    self.game.header="Press Space to confirm!"

                elif len(self.selected)==1:
                    self.game.text_ind=1
                    self.game.selecting_player=True
                    self.fil=self.ind
                    self.image=self.player_images[self.fil][self.col]
                    print(self.selected)


        elif self.game.selecting_player:

            if len(self.team)==2 and (self.col!=self.team[-1] and self.col!=self.team[-2]):
                self.team.append(self.col)
                self.game.text_ind=-1
                self.scroll_ind=0

            elif len(self.team)<3:
                try:
                    if self.team[-1]== self.col or self.col== self.team[-2]:
                        self.game.text_ind=3
                    else:
                        self.team.append(self.col)
                        self.game.text_ind=1
                        print(self.team)

                except:
                    self.team.append(self.col)
                    print(self.team)
                    self.game.text_ind=1

            elif len(self.team)==3:
                self.select_keeper()
                self.selecting_keeper=True


    def select_keeper(self):
        self.col=0
        self.image=self.keeper_images[self.fil][self.col]

    def scroll(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()
        self.game.header="These are your players!"
        if now- self.timer>500:
            self.timer= now

            if self.scroll_ind==0:
                self.image=self.player_images[self.fil][self.team[self.scroll_ind]]
                self.scroll_ind+=1

            elif self.scroll_ind==len(self.team):
                self.scroll_ind=0
                self.image=self.keeper_images[self.fil][self.keepers[0]]
            else:
                self.image=self.player_images[self.fil][self.team[self.scroll_ind]]
                self.scroll_ind+=1







"""
            if keys[pg.K_BACKSPACE] and now- self.timer>250:
                self.game.timer= now

                if len(self.selected)==0:
                    pass
                else:
                    self.selected.remove(self.selected[-1])

            if keys[pg.K_m] and now - self.timer>250:
                self.game.timer= now

                print(self.selected)
"""

class player(pg.sprite.Sprite): #Crea el jugador

    def __init__(self,game): #Asignacion de las variables necesarias para el funcionamiento
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.changing= False
        self.current_frame= 0
        self.last_update= 0
        self.last_dir=0

        self.load_images()

        self.image= self.right_frames[self.current_frame]

        self.rect= self.image.get_rect()
        self.rect.center=(300,300)
        self.pos= vec(300,300)
        self.vel= vec(0,0)
        self.acc= vec(0,0)

    def load_images(self): #Carga todas las imagenes de los movimientos del jugador

        self.right_frames = [Image1.get_image(0,0,372,572), Image2.get_image(0,0,372,572)]

        self.left_frames = [Image1.get_image(0,0,372,572), Image2.get_image(0,0,372,572)]


    def animate(self): #Animacion del jugador
        now = pg.time.get_ticks()

        if self.changing:
            if now - self.last_update>100:
                self.last_update=now
                self.current_frame= (self.current_frame + 1) % len(self.right_frames)
                if self.vel.x > 0:
                    self.image= self.right_frames[self.current_frame]
                else:
                    self.image= self.left_frames[self.current_frame]

        if not self.walking and not self.jumping:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = 0
                if self.last_dir==0:
                    self.image = self.right_frames[0]
                else:
                    self.image = self.left_frames[0]

                    #Credito al canal KidsCanCode

    def update(self): #Actualiza el jugador en movimientos
        self.animate()
        self.acc= vec(0,0)
        keys= pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            self.changing
            self.last_dir=1

        if keys[pg.K_RIGHT]:
            self.changing
            self.last_dir=0

        self.acc += self.vel * PLAYER_FRICC
        self.vel += self.acc
        if abs(round(self.vel.x,5)) <  0.1 :
            self.vel.x=0
            self.walking=False
