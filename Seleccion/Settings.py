#SETTINGS#
import pygame

# ------------------------------ VARIABLES PARA INTERFAZ ---------------------------------
WIDTH= 800
HEIGHT= 500

FPS=60

TITLE= "Ghost Goalkeeper"

#Colores
WHITE= (255,255,255)
BLACK= (0,0,0)
RED= (255,0,0)

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

Clock = pygame.time.Clock()

COLORKEY= (255,9,255)

Title_Text = pygame.font.Font('Fonts/60s Scoreboard.ttf', 46)
Small_Text = pygame.font.Font('Fonts/Exo-Medium.otf', 14)
Medium_Text = pygame.font.Font('Fonts/Exo-Medium.otf', 16)
Large_Text = pygame.font.Font('Fonts/Exo-Medium.otf', 26)

# ------------------------------ IMAGENES ---------------------------------
Background = pygame.image.load('Imgs/stadium.png')
Background_img ='Imgs/stadium.png'
Photo_Karina = pygame.image.load("Imgs/photo_karina.png")
Photo_Eduardo = pygame.image.load("Imgs/photo_eduardo.png")

# ------------------------------ SPRITESHEETS ---------------------------------

REFEREES = "Imgs/referee_sheet.png"
LOGOS= "Seleccion/Logos.png"
#Real Madrid
REAL= "Seleccion/Real Madrid.png"
#Barcelona
BARCELONA= "Seleccion/Barcelona.png"
#Bayern
BAYERN= "Seleccion/Bayern.png"

KEEPERS="Seleccion/Keepers.png"
REFEREE = ""

IMAGES=[(0,0,372,572)]
# ------------------------------ TEXT LISTS ---------------------------------
Team_Names=["Barcelona FC","Real Madrid FC","Bayern Munich FC"]


Player_Names=[  ["Lionel Messi","Neymar Jr.","Luis Suarez","Andres Iniesta","Pique","Sergio Busquets","Turan"],
                ["Sergio Ramos","Cristiano Ronaldo","Isco","Karim Benzema","Gareth Bale","James Rodriguez","Marco Asensio"],
                ["Lewandoski","Ribery","Robben","Thiago","Muller","Vidal","Costa"]]

Keeper_Names=[["Ter Stegen","Cillissen","Masip"],["Keylor Navas","Kiko Casilla","Ruben Yañez"],["Neuer","Ulreich","Starke"]]


