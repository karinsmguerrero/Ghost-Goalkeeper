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
        self.selecting_team1=True
        self.selecting_team2=False
        self.load_images()
        self.image= self.images_list[self.ind]
        self.image.set_colorkey(RED)

        pg.transform.scale(self.image,(40,40))

        self.rect= self.image.get_rect()
        self.rect.center= vec(x,y)
        self.timer=0
        self.team1=[]
        self.selected1=[]
        self.keepers1=[]

        self.team2=[]
        self.selected2=[]
        self.keepers2=[]

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

        Barcelona= BARCELONA
        Bar_sheet= Spritesheet(Barcelona)

        Bayern= BAYERN
        Bayern_sheet= Spritesheet(Bayern)

        Keepers= KEEPERS
        Keeper_sheet= Spritesheet(Keepers)

                            #Barcelona
        self.player_images=[[Bar_sheet.get_image(0,0,418,413), Bar_sheet.get_image(893,0,418,413),
                            Bar_sheet.get_image(1901,0,418,413),Bar_sheet.get_image(2593,0,418,413),
                            Bar_sheet.get_image(3681,0,418,413),Bar_sheet.get_image(4639,0,418,413),
                            Bar_sheet.get_image(5281,0,418,413)],
                            #Real Madrid
                            [Realsheet.get_image(0,0,418,413),Realsheet.get_image(421,0,418,413),
                            Realsheet.get_image(876,0,418,413),Realsheet.get_image(1319,0,418,413),
                            Realsheet.get_image(1758,0,418,413),Realsheet.get_image(2176,0,418,413),
                            Realsheet.get_image(2597,0,418,413)],
                            #Bayern
                            [Bayern_sheet.get_image(0,0,418,413),Bayern_sheet.get_image(691,0,418,413),Bayern_sheet.get_image(1397,0,418,413),Bayern_sheet.get_image(1995,0,418,413),Bayern_sheet.get_image(2641,0,418,413),Bayern_sheet.get_image(3323,0,418,413),Bayern_sheet.get_image(4113,0,418,413)]]

                            #Barcelona
        self.keeper_images=[[Keeper_sheet.get_image(1800,0,418,413),Keeper_sheet.get_image(2464,0,418,413                    ), Keeper_sheet.get_image(3339,0,418,413)],
                            #Real Madrid
                            [Keeper_sheet.get_image(0,0,418,413),Keeper_sheet.get_image(431,0,418,413),
                            Keeper_sheet.get_image(1210,2,418,413)],
                            #Bayern
                            [Keeper_sheet.get_image(4091,0,418,413),Keeper_sheet.get_image(4771,0,418,413),Keeper_sheet.get_image(6073,0,418,413)]]


        for image in self.player_images[0]:
            image.set_colorkey(COLORKEY)

        for image in self.player_images[1]:
            image.set_colorkey(COLORKEY)

        for image in self.player_images[2]:
            image.set_colorkey(COLORKEY)

        for image in self.keeper_images[1]:
            image.set_colorkey(COLORKEY)



    def animate_right(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()
        if self.selecting_team1:
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
        if self.selecting_team1:
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
        if self.selecting_team1:
            if self.selecting_keeper:
                if len(self.keepers1)<1:
                    self.keepers1.append(self.col)
                else:
                    self.game.showing= True

            elif self.game.selecting and not self.game.selecting_player:

                    if len(self.selected1)<1:

                        self.selected1.append(self.ind)
                        self.game.header="Press Space to confirm!"

                    elif len(self.selected1)==1:
                        self.game.text_ind=1
                        self.game.selecting_player=True
                        self.fil=self.ind
                        self.image=self.player_images[self.fil][self.col]
                        print(self.selected1)


            elif self.game.selecting_player:

                if len(self.team1)==2 and (self.col!=self.team1[-1] and self.col!=self.team1[-2]):
                    self.team1.append(self.col)
                    self.game.text_ind=-1
                    self.scroll_ind=0

                elif len(self.team1)<3:
                    try:
                        if self.team1[-1]== self.col or self.col== self.team1[-2]:
                            self.game.text_ind=3
                        else:
                            self.team1.append(self.col)
                            self.game.text_ind=1
                            print(self.team1)

                    except:
                        self.team1.append(self.col)
                        print(self.team1)
                        self.game.text_ind=1

                elif len(self.team1)==3:
                    self.select_keeper()
                    self.selecting_keeper=True

        if self.selecting_team2:
            if self.selecting_keeper:
                if len(self.keepers2)<1:
                    self.keepers1.append(self.col)
                else:
                    self.game.showing= True

            elif self.game.selecting and not self.game.selecting_player:

                    if len(self.selected2)<1:

                        self.selected2.append(self.ind)
                        self.game.header="Press Space to confirm!"

                    elif len(self.selected2)==1:
                        self.game.text_ind=1
                        self.game.selecting_player=True
                        self.fil=self.ind
                        self.image=self.player_images[self.fil][self.col]
                        print(self.selected2)


            elif self.game.selecting_player:

                if len(self.team2)==2 and (self.col!=self.team2[-1] and self.col!=self.team2[-2]):
                    self.team2.append(self.col)
                    self.game.text_ind=-1
                    self.scroll_ind=0

                elif len(self.team2)<3:
                    try:
                        if self.team2[-1]== self.col or self.col== self.team2[-2]:
                            self.game.text_ind=3
                        else:
                            self.team2.append(self.col)
                            self.game.text_ind=1
                            print(self.team2)

                    except:
                        self.team2.append(self.col)
                        print(self.team2)
                        self.game.text_ind=1

                elif len(self.team2)==3:
                    self.select_keeper()
                    self.selecting_keeper=True


    def select_keeper(self):
        if self.selecting_team1:
            self.col=0
            self.image=self.keeper_images[self.fil][self.col]

    def scroll(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()
        self.game.header="These are your players!"
        if self.selecting_team1:
            if now- self.timer>500:
                self.timer= now

                if self.scroll_ind==0:
                    self.image=self.player_images[self.fil][self.team1[self.scroll_ind]]
                    self.scroll_ind+=1

                elif self.scroll_ind==len(self.team1):
                    self.scroll_ind=0
                    self.image=self.keeper_images[self.fil][self.keepers1[0]]
                else:
                    self.image=self.player_images[self.fil][self.team1[self.scroll_ind]]
                    self.scroll_ind+=1
        elif self.selecting_team2:
            pass
