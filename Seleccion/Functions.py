import pygame as pg

#Todas estas funciones trabajan con objetos

def draw_text(self, text, size, color, x, y): #Funcion para crear texto
        font= pg.font.Font(self.font_name, size)
        text_surface= font.render(text, True, color)
        text_rect= text_surface.get_rect()
        text_rect.midtop= (x,y)
        self.screen.blit(text_surface, text_rect)

def wait_for_key(self): #Funcion que espera el evento de presionar una tecla
        waiting=True
        keys= pg.key.get_pressed()
        now= pg.time.get_ticks()
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type== pg.QUIT:
                    waiting= False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        waiting= False
                    if event.key == pg.K_m:
                        self.show_start_screen()
                    if event.key == pg.K_c:
                        self.show_credits()
                    if event.key == pg.K_h:
                        self.show_highscores()

class Spritesheet: #Funcion para cargar imagenes de un spritesheet
    def __init__(self,filename):
        self.spritesheet= pg.image.load(filename)

    def get_image(self, x, y, width, height):
        image= pg.Surface((width, height))
        image.blit(self.spritesheet, (0,0), (x, y, (width)*2, (height)*2))

        return image


"""Uso de Class Spritesheet:


Antes de cargar una imagen, se debe declarar el path del cual se va a cargar la imagen. Esta debe estar incluida en la misma carpeta que los archivos para el funciona_
miento del juego.
Ejemplo:

        Ejemplo= pg.image.load("Estoesunaimagen.png")
        imagen= Spritesheet(Ejemplo)

        Para cargar un sprite:

        imagen.get_image(PosicionX, PosicionY, Ancho, Largo)

        """
