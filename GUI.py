import pygame
from Seleccion.Main import Game
from Seleccion.Settings import *
from Seleccion.Classes import Referee

# Inicia modulo de pygame
pygame.init()

# -------------------------- MUSICA ------------------------------------
pygame.mixer.init()
pygame.mixer.music.load('Sounds/UEFA_Champions_League_Anthem.ogg')

# ------------------- VARIABLES PARA INTERFAZ --------------------------
#region

White = (255, 255, 255)
Black = (0, 0, 0)
Turquoise = (45, 195, 192)
Bright_turquoise = (52, 237, 233)
Blue = (10, 36, 118)
Bright_blue = (0, 0, 255)
Sky_blue = (112, 158, 210)
Dark_blue = (22, 70, 136)

Display_width = 800
Display_height = 500

Title_Text = pygame.font.Font('Fonts/60s Scoreboard.ttf', 46)
Small_Text = pygame.font.Font('Fonts/Exo-Medium.otf', 14)
Medium_Text = pygame.font.Font('Fonts/Exo-Medium.otf', 18)
Large_Text = pygame.font.Font('Fonts/Exo-Medium.otf', 26)

Clock = pygame.time.Clock()
GameClass = Game()
#endregion

# ------------------------------ IMAGENES ---------------------------------
Background = pygame.image.load('Imgs/stadium.png')

# -------------------------------- DISPLAY ----------------------------------
GameDisplay = pygame.display.set_mode((Display_width, Display_height))
pygame.display.set_caption('Ghost Goalkeeper')


# -------------------------------- MENU ------------------------------------
def game_menu():
    """ ================================================================
                Instituto Tecnológico de Costa Rica
                Ingeniería en computadores
                Nombre del programa: Ghost Goalkeeper
                Autores:
                    Karina Martínez Guerrero
                    Eduardo Quiroga Alfaro
                Profesor: Milton Villegas Lemus
                Lenguaje: Python 3.6
                Version de Pygame: 1.9.3
                Versión: 1.0
                Fecha de creación: 31/05/2017
                Descripcion: Proyecto de introduccion a la programación..
                Requerimientos:
                    Python 3.6
                    Pygame 1.9.3
                    Fuentes:
                        OCRAExtended.ttf
                        Budmo Jiggler.ttf
                    Sonido:
                        Title_Screen_music.ogg
                        level_music.ogg

                ================================================================
    """
    Display = True
    #Codigo por si acaso
    pygame.mixer.music.load('Sounds/UEFA_Champions_League_Anthem.ogg')

    # comprueba que no haya musica reproduciendose
    if pygame.mixer.music.get_busy() == False:
    # reproduce la musica, el -1 hace el bucle infinito
        pygame.mixer.music.play(-1)

    GameDisplay.blit(Background, (0, 0))

    while Display:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()

            Menu_bar = pygame.draw.rect(GameDisplay, Sky_blue, [0, 0, Display_width, 50])
            button("Menu", 0, 0, 100, 50, Sky_blue, Dark_blue, game_menu)
            button("Aboout", 100, 0, 100, 50, Sky_blue, Dark_blue, game_about)

            message_display('Ghost Goalkeeper', Title_Text, Display_width // 2, Display_height // 3)

            button("New game", (Display_width // 2 - 100), 400, 200, 50, Dark_blue, Blue, game_settings)

        # actualizar la pantalla

        pygame.display.update()
        # reloj que controla los frames-per-second
        Clock.tick(30)

#---------------------------GUI FUNCTIONS---------------------------
#region
def game_exit_confirmation():
    """ Objetivo: funcion que crea una ventana al presionar el boton de cerrar, para elegir
        entre reiniciar la partida, salir del juego, o ir al menu principal
        Entradas: clicks de mouse"""
    Display = True

    while Display:
        for event in pygame.event.get():
            GameDisplay.fill(Black)
            message_display('¿Desea salir del juego?', Medium_Text, Display_width // 2, 200)
            button("Salir", 30, 400, 100, 50, Turquoise, Bright_turquoise, game_exit)
            button("Ir al inicio", 160, 400, 140, 50, Turquoise, Bright_turquoise, game_menu)
            button("Reiniciar partida", 320, 400, 150, 50, Turquoise, Bright_turquoise, game_start)

            # actualizar la pantalla
            pygame.display.update()
            # reloj que controla los frames-per-second
            Clock.tick(30)

def game_exit():
    pygame.mixer.music.stop()
    pygame.quit()
    quit()

def game_about():
    """ Objetivo: funcion que crea una ventana con informacion acerca del juego"""

    Display = True
    Photo_Karina = pygame.image.load("Imgs/photo_karina.png")
    Photo_Eduardo = pygame.image.load("Imgs/photo_eduardo.png")
    while Display:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
            GameDisplay.fill(Black)
            Menu_bar = pygame.draw.rect(GameDisplay, Sky_blue, [0, 0, Display_width, 50])
            # button(text, x_coord, y_coord, btn_widht, btn_height, color, hover_color, action=None)
            button("Inicio", 0, 0, 100, 50, Sky_blue, Dark_blue, game_menu)
            button("Acerca de", 100, 0, 100, 50, Sky_blue, Dark_blue, game_about)

            message_display('Instituto Tecnológico de Costa rica', Small_Text, Display_width // 2, 100)
            message_display('Ingeniería en computadores', Small_Text, Display_width // 2, 120)
            message_display('Profesor Milton Villegas Lemus', Small_Text, Display_width // 2, 140)
            message_display('Karina Martínez Guerrero', Small_Text, Display_width // 2, 160)
            message_display('2017102001', Small_Text, Display_width // 2, 180)
            message_display('Eduardo Quiroga Alfaro', Small_Text, Display_width // 2, 200)
            message_display('2017079534', Small_Text, Display_width // 2, 220)
            message_display('V 1.0', Small_Text, Display_width // 2, 240)
            message_display('Última modificación: 00/06/2017', Small_Text, Display_width // 2, 260)

            GameDisplay.blit(Photo_Karina, (200, 280))
            GameDisplay.blit(Photo_Eduardo, (400, 280))

        # actualizar la pantalla
        pygame.display.update()
        # reloj que controla los frames-per-second
        Clock.tick(30)

def button(Text, X_coord, Y_coord, Btn_width, Btn_height, Color, Hover_color, Action=None):
    """ Objetivo: funcion que recrea el comportamiento de un botón
        Entradas: texto con el mensaje, coordenada x del rectangulo, coordenada y del rectangulo,
        ancho del rectangulo, alto del rectangulo, color del rectangulo, color al pasar el puntero sobre el botón,
        funcion que debe ejecutar
        Salidas: rectangulo con la funcionalidad de un botón
        Referencias:
            VIDEO: Game Development in Python 3 With PyGame - 11 - Buttons p. 1
            URL: https://www.youtube.com/watch?v=jh_m-Eytq0Q """

    # obtener la posicion del puntero y los eventos click
    Mouse = pygame.mouse.get_pos()
    Click = pygame.mouse.get_pressed()

    # comprobar si el puntero pasa sobre el boton
    if X_coord + Btn_width  > Mouse[0] > X_coord and Y_coord + Btn_height > Mouse[1] > Y_coord:
        pygame.draw.rect(GameDisplay, Hover_color, (X_coord, Y_coord, Btn_width, Btn_height))
        if Click[0] == 1 and Action != None:
            Action()
    else:
        pygame.draw.rect(GameDisplay, Color, (X_coord, Y_coord , Btn_width, Btn_height))

    #tomar el texto y aplicarlo a un rectangulo para mostrarlo sobre el botón
    textSurf, textRect = text_objects(Text, Small_Text)
    textRect.center = ((X_coord + (Btn_width / 2)), (Y_coord + (Btn_height / 2)))
    GameDisplay.blit(textSurf, textRect)

def message_display(text, size, x_center, y_center):
    """ Objetivo: funcion que recibe una cadena de texto, la convierte en texto y la presenta en un rectangulo
            Entradas: texto con el mensaje, tamaño y fuente del texto, coordenada x del centro, coordenada y del texto
            Salidas: texto presentado como si fuera una imagen
            Referencias:
            VIDEO: Game Development in Python 3 With PyGame - 11 - Buttons p. 1
            URL: https://www.youtube.com/watch?v=jh_m-Eytq0Q """
    # tomar el texto y su contenedor
    textSurface, textArea = text_objects(text, size)
    # definir el centro de la figura
    textArea.center = ((x_center), (y_center))
    # dibujar el texto en el surface
    GameDisplay.blit(textSurface, textArea)

    pygame.display.update()

def text_objects(text, font):
    """ Objetivo: funcion que toma el texto y lo presenta como imagen
            Entradas: texto con el mensaje, tamaño y fuente del texto
            Salidas: texto presentado como imagen
            Referencias:
            VIDEO: Game Development in Python 3 With PyGame - 11 - Buttons p. 1
            URL: https://www.youtube.com/watch?v=jh_m-Eytq0Q """
    textSurface = font.render(text, True, White)
    return textSurface, textSurface.get_rect()

#endregion

def game_start(player1, player2, change_mode):
    running = True
    GameDisplay.blit(Background, (0, 0))
    message_display("Game Settings", Large_Text, Display_width // 2, 30)
    #carga el spritesheet de los logos, importado de settings
    logo_sheet = pygame.image.load("Imgs/mini_logo_sheet.png")
    logo_sheet.set_colorkey((255,9,255))
    message_display("Player 1", Large_Text, 200, 100)
    message_display("Player 2", Large_Text, 600, 100)
    player1_logo = player1[0][0]
    player2_logo = player2[0][0]

    player1_team = player1[1]
    player2_team = player2[1]

    player1_keeper = player1[2]
    player2_keeper = player2[2]
    print(player1_logo, player1_team, player1_keeper)

    # Despliega el logo del equipo seleccionado por el jugador 1
    GameDisplay.blit(logo_sheet, (100, 130), (player1_logo * 200, 0, 200, 200))
    # Despliega los nombres de los jugadores, obteniendolos de una matriz importada de Settings
    message_display(Player_Names[player1_logo][player1_team[0]], Large_Text, 200, 360)
    message_display(Player_Names[player1_logo][player1_team[1]], Large_Text, 200, 390)
    message_display(Player_Names[player1_logo][player1_team[2]], Large_Text, 200, 420)
    message_display(Keeper_Names[player1_logo][player1_keeper[0]], Large_Text, 200, 450)
    message_display(change_mode[0], Large_Text, 200, 480)

    # Despliega el logo del equipo seleccionado por el jugador 1
    GameDisplay.blit(logo_sheet, (500, 130), (player2_logo * 200, 0, 200, 200))
    # Despliega los nombres de los jugadores, obteniendolos de una matriz importada de Settings
    message_display(Player_Names[player2_logo][player1_team[0]], Large_Text, 600, 360)
    message_display(Player_Names[player2_logo][player2_team[1]], Large_Text, 600, 390)
    message_display(Player_Names[player2_logo][player2_team[2]], Large_Text, 600, 420)
    message_display(Keeper_Names[player2_logo][player2_keeper[0]], Large_Text, 600, 450)
    message_display(change_mode[1], Large_Text, 600, 480)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
        pygame.display.update()
        Clock.tick(30)

def game_change_selector():
    options = ["Auto", "Manual"]
    Running = True
    option = 0
    mode_selected = []
    GameDisplay.blit(Background, (0,0))
    message_display("Choose the change mode for your team", Large_Text, Display_width//2, 100)

    pygame.draw.rect(GameDisplay, Dark_blue, (250, 300, 100, 50))
    message_display("Auto", Medium_Text, 300, 325)

    pygame.draw.rect(GameDisplay, Sky_blue, (450, 300, 100, 50))
    message_display("Manual", Medium_Text, 500, 325)

    Current_player = 1
    while Running:

        if Current_player == 1:
            message_display("Player 1", Large_Text, Display_width//2, 160)
        elif Current_player == 2:
            message_display("Player 2", Large_Text, Display_width // 2, 160)
        for event in pygame.event.get():
            if Current_player == 2:
                message_display("Player 2", Large_Text, Display_width // 2, 160)
            if event.type == pygame.QUIT:
                game_exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    option = 1
                    pygame.draw.rect(GameDisplay, Sky_blue, (250, 300, 100, 50))
                    message_display("Auto", Medium_Text, 300, 325)

                    pygame.draw.rect(GameDisplay, Dark_blue, (450, 300, 100, 50))
                    message_display("Manual", Medium_Text, 500, 325)
                elif event.key == pygame.K_LEFT:
                    option = 0
                    pygame.draw.rect(GameDisplay, Dark_blue, (250, 300, 100, 50))
                    message_display("Auto", Medium_Text, 300, 325)

                    pygame.draw.rect(GameDisplay, Sky_blue, (450, 300, 100, 50))
                    message_display("Manual", Medium_Text, 500, 325)
                elif event.key == pygame.K_SPACE:
                    if Current_player == 1:
                        mode_selected.append(options[option])
                        Current_player = 2
                    else:
                        mode_selected.append(options[option])
                        return mode_selected

        pygame.display.update()
        Clock.tick(30)


def select_referee():
    Referee_Names = ["Karina Martínez", "Eduardo Quiroga"]
    Referee_sheet = pygame.image.load("Imgs/referee_sheet.png")
    Referee_sheet.set_colorkey((255,9,255))

    pos = 0
    running = True
    GameDisplay.blit(Background, (0, 0))
    message_display("Select a referee!",Large_Text, Display_width//2, 20)
    GameDisplay.blit(Referee_sheet, (Display_width//2 - 200,70), (400 * pos, 0, 400,400))
    message_display(Referee_Names[pos], Large_Text, Display_width//2, 50)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if pos == 0:
                        pos = 1
                    else:
                        pos = 0
                    GameDisplay.blit(Background, (0, 0))
                    message_display(Referee_Names[pos], Large_Text, Display_width//2, 50)
                    GameDisplay.blit(Referee_sheet, (Display_width//2 - 200,70), (400 * pos, 0, 400,400))
                elif event.key == pygame.K_RIGHT:
                    if pos == 1:
                        pos = 0
                    else:
                        pos = 1
                    GameDisplay.blit(Background, (0, 0))
                    message_display(Referee_Names[pos], Large_Text, Display_width // 2, 50)
                    GameDisplay.blit(Referee_sheet, (Display_width//2 - 200,70), (400 * pos, 0, 400, 400))
                elif event.key == pygame.K_SPACE:
                    return Referee_Names[pos]
        pygame.display.update()
        Clock.tick(30)

def game_settings():
    GameClass.REFEREE = select_referee()
    current_player = 1
    player_1_team = []
    player_2_team = []
    change_mode = []
    while GameClass.running:
        if current_player == 2:
            if GameClass.finish:
                player_2_team.append(GameClass.selector.selected)
                player_2_team.append(GameClass.selector.team)
                player_2_team.append(GameClass.selector.keepers)
                change_mode = game_change_selector()
                game_start(player_1_team, player_2_team, change_mode)

        GameClass.new()

        if GameClass.finish:
            player_1_team.append(GameClass.selector.selected)
            player_1_team.append(GameClass.selector.team)
            player_1_team.append(GameClass.selector.keepers)
            GameClass.new()
            current_player = 2

#-----------------MAIN-------------------------------
game_menu()
#select_referee()
#game_start([0, [1,2,3],1],[2, [1,2,3], 0])
#game_change_selector()

