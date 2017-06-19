"Classes"
import pygame as pg
import random
from Functions import *
from Settings import *
vec= pg.math.Vector2


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
        self.rect= self.image.get_rect()
        self.rect.center= vec(x,y)
        self.timer=0
        self.team1=[]
        self.selected1=[]
        self.keepers1=[]

        self.team=[]

        self.team2=[]
        self.selected2=[]
        self.keepers2=[]

    def load_images(self):
        #Logos
        Logos=LOGOS
        Logosheet= Spritesheet(Logos)

        Barcelona=Logosheet.get_image(0,0,418,418)

        Barcelona.set_colorkey(COLORKEY)

        self.images_list=[Barcelona,
        Logosheet.get_image(515-((811-515)/2)/2,0,418,418),
        Logosheet.get_image(921,0,418,418)]

        for image in self.images_list:
            image.set_colorkey((255,9,255))


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
            self.team=self.team1
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


class Ref_Selector(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game=game
        Logos=LOGOS
        self.pos= vec(x,y)
        self.ind=0
        self.selected=False
        self.load_images()
        self.image= self.images_list[self.ind]

        pg.transform.scale(self.image,(40,40))

        self.rect= self.image.get_rect()
        self.rect.center= vec(x,y)
        self.timer=0
        self.referee=[]


    def load_images(self):
        Refs= Spritesheet(REFEREES)

        self.images_list=[Refs.get_image(0,0,400,400),Refs.get_image(400,0,400,400)]

        for image in self.images_list:
            image.set_colorkey(COLORKEY)




    def animate_right(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()

        if now-self.timer>250 and not self.selected:
            self.timer=now
            if self.ind==len(self.images_list)-1:
                self.ind=0
                self.image= self.images_list[self.ind]
            else:
                self.ind+=1
                self.image= self.images_list[self.ind]


    def animate_left(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()
        if now-self.timer>250 and not self.selected:
            self.timer=now
            if self.ind==0:
                self.ind=len(self.images_list)-1
                self.image= self.images_list[self.ind]
            else:
                self.ind-=1
                self.image= self.images_list[self.ind]


    def selection(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()

        if now-self.timer>250:
            self.selected=True
            self.referee.append(self.ind)


class Coin(pg.sprite.Sprite):

    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game=game
        self.pos= vec(x,y)
        self.ind=0
        self.load_images()
        self.image= self.images_list[self.ind]
        self.rect= self.image.get_rect()
        self.rect.center= vec(x,y)
        self.timer=0
        self.down=False
        self.stall=False


    def load_images(self):

        Coin_sheet= Spritesheet("coin_flip.png")

        self.images_list=[Coin_sheet.get_image(0,0,98,98),Coin_sheet.get_image(0,124,98,219-124),Coin_sheet.get_image(0,245,98,309-245),
        Coin_sheet.get_image(0,333,98,359-333),Coin_sheet.get_image(0,383,98,447-383),Coin_sheet.get_image(0,470,98,566)]

        for image in self.images_list:
            image.set_colorkey(BLACK)


    def animate(self):
        now= pg.time.get_ticks()


        if self.pos.y>600:
            self.stall=True


        elif now-self.timer>50 and self.pos.y>=250 and not self.down:
            self.timer=now
            if self.ind!=len(self.images_list)-1:
                self.ind+=1
                self.image= self.images_list[self.ind]
                self.pos.y-=20
                self.rect.center=self.pos
            else:
                self.ind=0
                self.image= self.images_list[self.ind]
                self.pos.y-=20
                self.rect.center=self.pos


        elif now-self.timer>50 and (self.pos.y<250 or self.down):
            self.down=True

            self.timer=now
            if self.ind!=len(self.images_list)-1:
                self.ind+=1
                self.image= self.images_list[self.ind]
                self.pos.y+=20
                self.rect.center=self.pos
            else:
                self.ind=0
                self.image= self.images_list[self.ind]
                self.pos.y+=20
                self.rect.center=self.pos
