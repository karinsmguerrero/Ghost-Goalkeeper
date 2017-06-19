import pygame as pg
import random
from Functions import *
from Settings import *
from Classes import *
import time
from indices import *
from Stats import *
from PlayerStats import *


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


        if keys[pg.K_m]:
            self.wait_for_key()

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
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))
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

    def show_about(self):
        Small_Text=20
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        self.draw_text('Instituto Tecnológico de Costa rica', Small_Text, WHITE, 350, 20)
        self.draw_text('Ingeniería en computadores', Small_Text, WHITE, 350 , 50)
        self.draw_text('Profesor Milton Villegas Lemus', Small_Text, WHITE,350, 80)
        self.draw_text('Karina Martínez Guerrero', Small_Text, WHITE, 250 , 110)
        self.draw_text('2017102001', Small_Text, WHITE, 250 , 140)
        self.draw_text('Eduardo Quiroga Alfaro', Small_Text, WHITE, 450 , 110)
        self.draw_text('2017079534', Small_Text, WHITE, 450, 140)
        self.draw_text('Version: 1.0', Small_Text, WHITE, 350 , 170)
        self.draw_text('Última modificación: 17/06/2017', Small_Text, WHITE,350,200)
        self.screen.blit(Eduardo,(350,300))
        self.screen.blit(Karina,(200,300))

        pg.display.flip()

    def show_menu(self):
        self.showing_menu=True
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        self.draw_text("Ghost Goalkeeper!",80,WHITE,350,50)

        self.draw_text("Press P to play!",40,WHITE,350,160)
        self.draw_text("Press A for About!",40,WHITE,350,320)
        self.draw_text("Press S for Stats!",40,WHITE,350,480)
        pg.display.flip()

    def show_stats(self):
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        #Stats
        self.draw_text("Games",20,WHITE,30,80+50)
        self.draw_text("Wins",20,WHITE,25,120+50)
        self.draw_text("Loses",20,WHITE,28,160+50)
        self.draw_text("Ties",20,WHITE,21,200+50)
        self.draw_text("Scored Goals",20,WHITE,53,240+50)
        self.draw_text("Failed Goals",20,WHITE,50,280+50)
        self.draw_text("Score Average",20,WHITE,54,320+50)
        self.draw_text("Fail Average",20,WHITE,50,360+50)

        #Header and Teams
        self.draw_text("Stat Board",40,WHITE,350,20)
        self.draw_text("Barcelona FC",30,WHITE,190,70)
        self.draw_text("Real Madrid FC",30,WHITE,370,70)
        self.draw_text("Bayern Munich FC",30,WHITE,590,70)

        #Stats 1

        Y=130

        Barcelona= statslist()[0]

        for stat in range(0,len(Barcelona)-2):
            self.draw_text(str(Barcelona[stat]),20,WHITE,190,Y)
            Y+=40

        if Barcelona[0]!=0:
            self.draw_text(str(Barcelona[4]/Barcelona[0]),20,WHITE,190,Y)
            self.draw_text(str(Barcelona[5]/Barcelona[0]),20,WHITE,190,Y+40)
        else:
            self.draw_text("0",20,WHITE,190,Y)
            self.draw_text("0",20,WHITE,190,Y+40)



        Y=130

        Real= statslist()[1]

        for stat in range(0,len(Real)-2):
            self.draw_text(str(Real[stat]),20,WHITE,370,Y)
            Y+=40

        if Real[0]!=0:
            self.draw_text(str(Real[4]/Real[0]),20,WHITE,370,Y)
            self.draw_text(str(Real[5]/Real[0]),20,WHITE,370,Y+40)
        else:
            self.draw_text("0",20,WHITE,370,Y)
            self.draw_text("0",20,WHITE,370,Y+40)

        Bayern= statslist()[2]

        Y=130

        for stat in range(0,len(Bayern)-2):
            self.draw_text(str(Bayern[stat]),20,WHITE,590,Y)
            Y+=40

        if Bayern[0]!=0:
            self.draw_text(str(Bayern[4]/Bayern[0]),20,WHITE,590,Y)
            self.draw_text(str(Bayern[5]/Bayern[0]),20,WHITE,590,Y+40)
        else:
            self.draw_text("0",20,WHITE,590,Y)
            self.draw_text("0",20,WHITE,590,Y+40)

        self.draw_text("Press 'R' to reset the stats",40,WHITE,350,500)


        self.draw_text("Press 'M' to go back to the menu",40,WHITE,350,600)


        pg.display.flip()

    def wait_for_key(self): #Funcion que espera el evento de presionar una tecla
        waiting=True
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()
        self.show_menu()
        self.showing_stats=False
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    waiting= False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        self.showing_stats=False
                        waiting= False
                    if event.key == pg.K_s:
                        self.showing_stats=True
                        self.show_stats()
                    if event.key == pg.K_a:
                        self.showing_stats=False
                        self.show_about()
                    if event.key== pg.K_m:
                        self.showing_stats=False
                        self.show_menu()
                    if self.showing_stats and event.key == pg.K_r:
                        clear()
                        self.show_stats()
                        self.showing_stats=False

Eduardo= pg.image.load("photo_eduardo.png")
Karina= pg.image.load("photo_karina.png")

class Referee_Selector:
    def __init__(self):
        #Inicializacion
        pg.init()
        pg.mixer.init()

        #Cargar elementos
        self.load_data()

        #Funcionamiento
        self.running=True
        self.timer=0
        self.clock= pg.time.Clock()
        self.screen= pg.display.set_mode((WIDTH,HEIGHT))
        self.font_name= pg.font.match_font(FONT_NAME)
        pg.display.set_caption(TITLE)

    def new(self):
        #Grupos
        self.all_sprites= pg.sprite.Group()

        #Seleccionador
        self.RefSelectorr= Ref_Selector(self,350,350)
        self.all_sprites.add(self.RefSelectorr)

        #Inicializacion del nuevo juego
        self.load_data()
        self.run()

    def load_data(self):
        pass

    def run(self):
        self.playing=True
        self.show_menu()
        self.wait_for_key()

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

        if keys[pg.K_SPACE] and self.RefSelectorr.selected and now-self.timer>250:
            self.running=False
            self.playing=False
        elif keys[pg.K_SPACE] and now-self.timer>250:
            self.timer=now
            self.RefSelectorr.selection()

        if keys[pg.K_RIGHT]:
            self.RefSelectorr.animate_right()

        if keys[pg.K_LEFT]:
            self.RefSelectorr.animate_left()

        if keys[pg.K_m]:
            self.wait_for_key()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        if self.RefSelectorr.selected:
            self.draw_text("Press Space to confirm!",40,WHITE,350,50)

        else:
            self.draw_text("Choose a referee!",40,WHITE,350,50)

        self.all_sprites.draw(self.screen)


        pg.display.flip()

    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            font= pg.font.Font(self.font_name, size)
            text_surface= font.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)

    def show_about(self):
        Small_Text=20
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        self.draw_text('Instituto Tecnológico de Costa rica', Small_Text, WHITE, 350, 20)
        self.draw_text('Ingeniería en computadores', Small_Text, WHITE, 350 , 50)
        self.draw_text('Profesor Milton Villegas Lemus', Small_Text, WHITE,350, 80)
        self.draw_text('Karina Martínez Guerrero', Small_Text, WHITE, 250 , 110)
        self.draw_text('2017102001', Small_Text, WHITE, 250 , 140)
        self.draw_text('Eduardo Quiroga Alfaro', Small_Text, WHITE, 450 , 110)
        self.draw_text('2017079534', Small_Text, WHITE, 450, 140)
        self.draw_text('Version: 1.0', Small_Text, WHITE, 350 , 170)
        self.draw_text('Última modificación: 17/06/2017', Small_Text, WHITE,350,200)
        self.screen.blit(Eduardo,(350,300))
        self.screen.blit(Karina,(200,300))

        pg.display.flip()

    def show_menu(self):
        self.showing_menu=True
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        self.draw_text("Ghost Goalkeeper!",80,WHITE,350,50)

        self.draw_text("Press P to play!",40,WHITE,350,160)
        self.draw_text("Press A for About!",40,WHITE,350,320)
        self.draw_text("Press S for Stats!",40,WHITE,350,480)
        pg.display.flip()

    def show_stats(self):
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        #Stats
        self.draw_text("Games",20,WHITE,30,80+50)
        self.draw_text("Wins",20,WHITE,25,120+50)
        self.draw_text("Loses",20,WHITE,28,160+50)
        self.draw_text("Ties",20,WHITE,21,200+50)
        self.draw_text("Scored Goals",20,WHITE,53,240+50)
        self.draw_text("Failed Goals",20,WHITE,50,280+50)
        self.draw_text("Score Average",20,WHITE,54,320+50)
        self.draw_text("Fail Average",20,WHITE,50,360+50)

        #Header and Teams
        self.draw_text("Stat Board",40,WHITE,350,20)
        self.draw_text("Barcelona FC",30,WHITE,190,70)
        self.draw_text("Real Madrid FC",30,WHITE,370,70)
        self.draw_text("Bayern Munich FC",30,WHITE,590,70)

        #Stats 1

        Y=130

        Barcelona= statslist()[0]

        for stat in range(0,len(Barcelona)-2):
            self.draw_text(str(Barcelona[stat]),20,WHITE,190,Y)
            Y+=40

        if Barcelona[0]!=0:
            self.draw_text(str(Barcelona[4]/Barcelona[0]),20,WHITE,190,Y)
            self.draw_text(str(Barcelona[5]/Barcelona[0]),20,WHITE,190,Y+40)
        else:
            self.draw_text("0",20,WHITE,190,Y)
            self.draw_text("0",20,WHITE,190,Y+40)



        Y=130

        Real= statslist()[1]

        for stat in range(0,len(Real)-2):
            self.draw_text(str(Real[stat]),20,WHITE,370,Y)
            Y+=40

        if Real[0]!=0:
            self.draw_text(str(Real[4]/Real[0]),20,WHITE,370,Y)
            self.draw_text(str(Real[5]/Real[0]),20,WHITE,370,Y+40)
        else:
            self.draw_text("0",20,WHITE,370,Y)
            self.draw_text("0",20,WHITE,370,Y+40)

        Bayern= statslist()[2]

        Y=130

        for stat in range(0,len(Bayern)-2):
            self.draw_text(str(Bayern[stat]),20,WHITE,590,Y)
            Y+=40

        if Bayern[0]!=0:
            self.draw_text(str(Bayern[4]/Bayern[0]),20,WHITE,590,Y)
            self.draw_text(str(Bayern[5]/Bayern[0]),20,WHITE,590,Y+40)
        else:
            self.draw_text("0",20,WHITE,590,Y)
            self.draw_text("0",20,WHITE,590,Y+40)

        self.draw_text("Press 'R' to reset the stats",40,WHITE,350,500)


        self.draw_text("Press 'M' to go back to the menu",40,WHITE,350,600)


        pg.display.flip()

    def wait_for_key(self): #Funcion que espera el evento de presionar una tecla
        waiting=True
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()
        self.show_menu()
        self.showing_stats=False
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    waiting= False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        self.showing_stats=False
                        waiting= False
                    if event.key == pg.K_s:
                        self.showing_stats=True
                        self.show_stats()
                    if event.key == pg.K_a:
                        self.showing_stats=False
                        self.show_about()
                    if event.key== pg.K_m:
                        self.showing_stats=False
                        self.show_menu()
                    if self.showing_stats and event.key == pg.K_r:
                        clear()
                        self.show_stats()
                        self.showing_stats=False

class Auto_Selector:
    def __init__(self,Team1,Players1,Keepers1,Team2,Players2,Keepers2):
        #Inicializacion
        pg.init()
        pg.mixer.init()

        #Cargar elementos
        self.load_data()
        self.Team1=Team1
        self.Players1=Players1
        self.Keepers1= Keepers1
        self.Team2=Team2
        self.Players2= Players2
        self.Keepers2= Keepers2

        #Funcionamiento
        self.already_selected=False
        self.text_choice=False
        self.running=True
        self.timer=0
        self.clock= pg.time.Clock()
        self.screen= pg.display.set_mode((WIDTH,HEIGHT))
        self.font_name= pg.font.match_font(FONT_NAME)
        pg.display.set_caption(TITLE)


    def load_data(self):
        self.team1_text=""
        self.team2_text=""
        self.ready=""

        self.selected_ind="Automatic"


    def new(self):

        self.all_sprites=pg.sprite.Group()

        self.coin=Coin(self,350,600)

        self.all_sprites.add(self.coin)


        self.run()

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
        self.coin.animate()

        if self.coin.stall:
            self.Local_selector()
            self.ready="Press Space to play!"

    def events(self):
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()



        if not self.text_choice:
            if keys[pg.K_SPACE]:
                self.timer=now
                self.text_choice=True
                self.ready=""

        elif self.text_choice:
            if keys[pg.K_a]:
                self.ready="Press Space to play!"
                self.selected_ind="Automatic"
            elif keys[pg.K_m]:
                self.ready="Press Space to play!"
                self.selected_ind="Manual"
            elif keys[pg.K_SPACE] and now-self.timer>250:
                self.running=False
                self.playing=False

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))

        if not self.text_choice:

            self.draw_text(self.ready,40,WHITE,350,10)

            self.draw_text("Player 1:",40,WHITE,200,50)
            self.draw_text(str(Team_Names[self.Team1[0]])+":",30,WHITE,200,100)

            self.draw_text(str(Player_Names[self.Team1[0]][self.Players1[0]]),30,WHITE,200,150)
            self.draw_text(str(Player_Names[self.Team1[0]][self.Players1[1]]),30,WHITE,200,200)
            self.draw_text(str(Player_Names[self.Team1[0]][self.Players1[2]]),30,WHITE,200,250)

            self.draw_text(str(Keeper_Names[self.Team1[0]][self.Keepers1[0]]),30,WHITE,200,300)

            self.draw_text(self.team1_text,30,WHITE,200,350)

            self.draw_text("Player 2:",40,WHITE,500,50)
            self.draw_text(str(Team_Names[self.Team2[0]])+":",30,WHITE,500,100)
            self.draw_text(str(Player_Names[self.Team2[0]][self.Players2[0]]),30,WHITE,500,150)
            self.draw_text(str(Player_Names[self.Team2[0]][self.Players2[1]]),30,WHITE,500,200)
            self.draw_text(str(Player_Names[self.Team2[0]][self.Players2[2]]),30,WHITE,500,250)

            self.draw_text(str(Keeper_Names[self.Team2[0]][self.Keepers2[0]]),30,WHITE,500,300)

            self.draw_text(self.team2_text,30,WHITE,500,350)

            self.all_sprites.draw(self.screen)

        else:
            self.screen.fill(BGCOLOR)
            self.screen.blit(pg.image.load("stadium.jpg"),(0,0))


            self.draw_text(self.ready,40,WHITE,350,10)


            self.draw_text("Press 'A' for automatic switching of the players!",30,WHITE,350,200)

            self.draw_text("Press 'M' for manual switching of the players!",30,WHITE,350,150)


            self.draw_text(str(self.selected_ind),30,WHITE,350,500)



        pg.display.flip()

    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            font= pg.font.Font(self.font_name, size)
            text_surface= font.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)

    def Local_selector(self):

        if not self.already_selected:
            self.team1_text=random.choice(["Local","Away"])

            if self.team1_text=="Local":
                self.already_selected=True
                self.team2_text="Away"
            elif self.team1_text=="Away":
                self.already_selected=True
                self.team2_text="Local"

logos= "s_logos.png"
Logos= Spritesheet(logos)

class Pen_shooter:
    def __init__(self,ind,local,team1,team2,players1,players2,keeper1,keeper2):
        #Inicializacion
        pg.init()
        pg.mixer.init()

        if local=="Local":
            #Jugadores
            self.team1_image=team1[0]
            self.players1_names=players1

            self.keeper1_name=keeper1[0]


            self.team2_image=team2[0]
            self.players2_names=players2
            self.keeper2_name=keeper2[0]
        else:
            self.team2_image=team1[0]
            self.players2_names=players1

            self.keeper2_name=keeper1[0]


            self.team1_image=team2[0]
            self.players1_names=players2
            self.keeper1_name=keeper2[0]

        #Cargar elementos
        self.load_data()

        #Funcionamiento
        self.switch=ind
        self.winner=0
        self.home_shooting=True
        self.nextpen=False
        self.shooted=False
        self.now_shooting=False
        self.shootingpens=True
        self.running=True
        self.timer=0
        self.clock= pg.time.Clock()
        self.screen= pg.display.set_mode((WIDTH,HEIGHT))
        self.font_name= pg.font.match_font(FONT_NAME)
        pg.display.set_caption(TITLE)

    def load_data(self):
        self.timer_text=0
        self.pens_text="Shooting!"
        self.goal_text=""

        self.team1=0
        self.team2=0
        self.pen_counter=1

        self.images_list=[Logos.get_image(15,53,195,150),Logos.get_image(4,270,195,150),Logos.get_image(320,191,185,150)]

        for image in self.images_list:
            image.set_colorkey(COLORKEY)

        self.ind=random.choice([0,1,2])


        self.player1_NameList=[]
        for i in self.players1_names:
            self.player1_NameList.append(Player_Names[self.team1_image][i])
        self.player1_NameList.append(Keeper_Names[self.team1_image][self.keeper1_name])
        self.playername1_ind=0

        self.player2_NameList=[]
        for i in self.players2_names:
            self.player2_NameList.append(Player_Names[self.team2_image][i])
        self.player2_NameList.append(Keeper_Names[self.team2_image][self.keeper2_name])
        self.playername2_ind=0

    def new(self):

        self.all_sprites=pg.sprite.Group()

        self.run()

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

        if self.shootingpens:
            if self.home_shooting:
                self.shoot=True
                if self.shoot:

                    if now-self.timer>1000:
                        if self.timer_text==3:
                            self.timer=now
                            self.timer_text+=1
                            pg.mixer.Channel(1).play(pg.mixer.Sound("short_whistle.ogg"))


                        elif self.timer_text<5:
                            self.timer=now
                            self.timer_text+=1
                            self.pens_text="Preparing!"


                        elif self.pens_text=="Preparing!":
                            self.pens_text="Shoot!"

                        else:
                            if now-self.timer>4000 and not self.now_shooting:
                                self.goal_text="Failed!"
                                self.shootingpens=False
                                self.nextpen=True
                                self.home_shooting=False
                                adding(self.team1_image,5)

                            elif keys[pg.K_0] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=False
                                self.playername1_ind+=1
                                if atajar(0) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team1+=1
                                    adding(self.team1_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))


                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team1_image,5)

                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_1] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=False
                                self.playername1_ind+=1

                                if atajar(1) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team1+=1
                                    adding(self.team1_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))

                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team1_image,5)

                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_2] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=False
                                self.playername1_ind+=1

                                if atajar(2) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.team1+=1
                                    self.nextpen=True
                                    adding(self.team1_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))

                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team1_image,5)

                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_3] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=False
                                self.playername1_ind+=1

                                if atajar(3) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team1+=1
                                    adding(self.team1_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))


                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team1_image,5)

                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_4] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=False
                                self.playername1_ind+=1

                                if atajar(4) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team1+=1
                                    adding(self.team1_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))

                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team1_image,5)

                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_5] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=False
                                self.playername1_ind+=1

                                if atajar(5) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team1+=1
                                    adding(self.team1_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))

                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team1_image,5)

                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))



            else:
                self.shoot=True
                if self.shoot:

                    if now-self.timer>1000:
                        if self.timer_text==3:
                            self.timer=now
                            self.timer_text+=1
                            pg.mixer.Channel(1).play(pg.mixer.Sound("short_whistle.ogg"))
                        elif self.timer_text<5:
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
                                self.home_shooting=True
                                self.pen_counter+=1
                                adding(self.team2_image,5)



                            elif keys[pg.K_0] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=True
                                self.pen_counter+=1
                                self.playername2_ind+=1


                                if atajar(0) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team2+=1
                                    adding(self.team2_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))
                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team2_image,5)
                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_1] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=True
                                self.pen_counter+=1
                                self.playername2_ind+=1

                                if atajar(1) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team2+=1
                                    adding(self.team2_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))

                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team2_image,5)
                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))


                            elif keys[pg.K_2] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=True
                                self.pen_counter+=1
                                self.playername2_ind+=1

                                if atajar(2) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.team2+=1
                                    self.nextpen=True
                                    adding(self.team2_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))

                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team2_image,5)
                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_3] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=True
                                self.pen_counter+=1
                                self.playername2_ind+=1

                                if atajar(3) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team2+=1
                                    adding(self.team2_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))



                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team2_image,5)
                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_4] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=True
                                self.pen_counter+=1
                                self.playername2_ind+=1

                                if atajar(4) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team2+=1
                                    adding(self.team2_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))



                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team2_image,5)
                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))

                            elif keys[pg.K_5] and not self.shooted:
                                self.shooted=True
                                self.now_shooting=True
                                self.timer=now
                                self.home_shooting=True
                                self.pen_counter+=1
                                self.playername2_ind+=1

                                if atajar(5) :
                                    self.goal_text="Goal!"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    self.team2+=1
                                    adding(self.team2_image,4)
                                    pg.mixer.Channel(2).play(pg.mixer.Sound("cheer.ogg"))


                                else:
                                    self.goal_text="Failed"
                                    self.shootingpens=False
                                    self.nextpen=True
                                    adding(self.team2_image,5)
                                    pg.mixer.Channel(1).play(pg.mixer.Sound("miss.ogg"))


        elif keys[pg.K_SPACE] and self.pen_counter>3:
            self.running=False
            self.playing=False

        elif self.nextpen and self.switch=="Manual" :
            self.pens_text="Waiting for next penalty!"
            if keys[pg.K_SPACE] and self.pen_counter<=3:
                self.shootingpens=True
                self.nextpen=False
                self.timer_text=0
                self.timer=now
                self.now_shooting=False
                self.shooted=False
                self.goal_text=""



            elif self.pen_counter>3:


                if self.team1>self.team2:
                    self.pens_text="Home wins!"
                elif self.team1==self.team2:
                    self.pens_text="Its a tie!"
                    if keys[pg.K_SPACE]:
                        self.running=False
                        self.playing=False
                        self.winner=2
                else:
                    self.pens_text="Away wins!"
                    if keys[pg.K_SPACE]:
                        self.running=False
                        self.playing=False
                        self.winner=1

        elif self.nextpen and self.switch=="Automatic":
            self.pens_text="Next penalty in 5 seconds!"
            if now-self.timer>6000 and self.pen_counter<=3:
                self.timer=now
                self.shootingpens=True
                self.nextpen=False
                self.timer_text=0
                self.timer=now
                self.now_shooting=False
                self.shooted=False
                self.goal_text=""
            elif self.pen_counter>3:
                if self.team1>self.team2:
                    self.pens_text="Home wins!"
                    if keys[pg.K_SPACE]:
                        self.running=False
                        self.playing=False
                elif self.team1==self.team2:
                    self.pens_text="Its a tie!"
                    if keys[pg.K_SPACE]:
                        self.running=False
                        self.playing=False
                        self.winner=2

                else:
                    self.pens_text="Away wins!"
                    if keys[pg.K_SPACE]:
                        self.running=False
                        self.playing=False
                        self.winner=1

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.screen.blit(pg.image.load("stadium.jpg"),(0,0))


        if (self.shootingpens or self.nextpen) and self.home_shooting:
            scoreboard= pg.image.load("scoreboard.jpg")
            self.screen.blit(scoreboard,(38,0))

            self.screen.blit(self.images_list[self.team1_image],(150,25))

            self.screen.blit(self.images_list[self.team2_image],(400,25))


            self.draw_text(str(self.timer_text),40,WHITE,350,480)
            self.draw_text(str(self.pens_text),40,WHITE,350,511)
            self.draw_text(str(self.goal_text),40,WHITE,350,550)
            if self.pen_counter<=3:
                self.draw_text(str(self.pen_counter),50,WHITE,350,256)
            else:
                self.draw_text(str(3),50,WHITE,350,256)


            self.draw_text(str(self.team1),80,WHITE,170,270)
            self.draw_text(str(self.team2),80,WHITE,530,270)

            self.draw_text(self.player1_NameList[self.playername1_ind],30,WHITE,170,600)
            self.draw_text(self.player2_NameList[-1],30,WHITE,530,600)

        else:
            scoreboard= pg.image.load("scoreboard.jpg")
            self.screen.blit(scoreboard,(38,0))

            self.screen.blit(self.images_list[self.team1_image],(150,25))

            self.screen.blit(self.images_list[self.team2_image],(400,25))


            self.draw_text(str(self.timer_text),40,WHITE,350,480)
            self.draw_text(str(self.pens_text),40,WHITE,350,511)
            self.draw_text(str(self.goal_text),40,WHITE,350,550)
            if self.pen_counter<=3:
                self.draw_text(str(self.pen_counter),50,WHITE,350,256)
            else:
                self.draw_text(str(3),50,WHITE,350,256)


            self.draw_text(str(self.team1),80,WHITE,170,270)
            self.draw_text(str(self.team2),80,WHITE,530,270)

            self.draw_text(self.player1_NameList[-1],30,WHITE,170,600)
            self.draw_text(self.player2_NameList[self.playername2_ind],30,WHITE,530,600)



        self.all_sprites.draw(self.screen)



        pg.display.flip()

    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            font= pg.font.Font(self.font_name, size)
            text_surface= font.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)

class Play_again:
    def __init__(self,text,home,away):
        pg.init()
        pg.mixer.init()
        self.running=True
        self.choice=False
        self.text=text
        self.clock=pg.time.Clock()
        self.screen= pg.display.set_mode((WIDTH,HEIGHT))
        self.font_name= pg.font.match_font(FONT_NAME)

        self.home=home
        self.away=away

    def new(self):
        self.run()
    def run(self):
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
            for event in pg.event.get(): #Cierra juego
                if event.type == pg.QUIT:
                    pg.quit()
    def events(self):
        keys=pg.key.get_pressed()

        if keys[pg.K_p]:
            self.choice=True
            self.running=False
            self.playing=False
            if self.text=="Home wins!":
                adding(self.home,1)
                adding(self.away,2)
            elif self.text=="Away wins!":
                adding(self.home,2)
                adding(self.away,1)
            else:
                adding(self.home,3)
                adding(self.away,3)



        if keys[pg.K_q]:
            if self.text=="Home wins!":
                adding(self.home,1)
                adding(self.away,2)
            elif self.text=="Away wins!":
                adding(self.home,2)
                adding(self.away,1)
            else:
                adding(self.home,3)
                adding(self.away,3)
            pg.quit()


    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.text,80,WHITE,350, 90)


        self.draw_text("Press P to play again!",80,WHITE,350, 350)


        self.draw_text("Press Q to quit!",80,WHITE,350, 450)

        pg.display.flip()

    def draw_text(self, text, size, color, x, y): #Funcion para crear texto
            font= pg.font.Font(self.font_name, size)
            text_surface= font.render(text, True, color)
            text_rect= text_surface.get_rect()
            text_rect.midtop= (x,y)
            self.screen.blit(text_surface, text_rect)

################################################################################




def game():

    pg.init()
    pg.mixer.init()
    pg.mixer.Channel(0).play(pg.mixer.Sound("UEFA_Champions_League_Anthem.ogg"))





    Team1=[]
    Selected1=[]
    Keepers1=[]

    Team2=[]
    Selected2=[]
    Keepers2=[]

    Arbitros=[]

    Ref=Referee_Selector()



    while Ref.running:
        Ref.new()


    G= Team_Selector()

    while G.running:
        G.new()



    Team1=G.selector.selected1
    Selected1=G.selector.team
    Keepers1=G.selector.keepers1

    H= Team_Selector()

    while H.running:
        H.new()

    Selected2=H.selector.team
    Team2=H.selector.selected1
    Keepers2=H.selector.keepers1

    adding(Team1[0],0)
    adding(Team2[0],0)

    A= Auto_Selector(Team1,Selected1,Keepers1,Team2,Selected2,Keepers2)

    while A.running:
        A.new()



    pg.mixer.Channel(0).stop()
    pg.mixer.music.load("ambience.ogg")
    pg.mixer.music.play(-1)

    pg.mixer.Channel(1).play(pg.mixer.Sound("long_whistle.ogg"))

    Penalties= Pen_shooter(A.selected_ind,A.team1_text,Team1,Team2,Selected1,Selected2,Keepers1,Keepers2)


    while Penalties.running:
        Penalties.new()

    Play= Play_again(Penalties.pens_text,Penalties.team1_image,Penalties.team2_image)

    while Play.running:
        Play.new()

    if Play.choice:
        return game()


game()
