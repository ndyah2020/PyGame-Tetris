from button import Button
import pygame
import sys
from tetris_game import TetrisGame
from game import Game
class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 620))
        self.BG = pygame.image.load("Background/background.jpg")
        self.Tetris = TetrisGame()
        self.game = Game()
        self.checkGame = True
        self.clickSound = pygame.mixer.Sound("sound/shooting.mp3")
        self.clickSound.set_volume(1)
    def get_font(self,size):
        return pygame.font.Font("Font/Atop-R99O3.ttf", size)
            
    def play(self):
        while self.Tetris.status: 
            self.Tetris.handle_events()
            self.Tetris.draw()
            self.Tetris.clock.tick(60)
            if not self.Tetris.checkMenu:
                self.Tetris.checkMenu = True
                self.main_menu()
            pygame.display.update()
    def volume(self):
        while True:
            self.screen.blit(self.BG, (0, 0))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            VOLUME_UP_BUTTON = Button(image=None, pos=(250, 200), 
                            text_input="Volume Up", font=self.get_font(30), 
                            base_color="White", hovering_color="#9400D3")
            VOLUME_DOWN_BUTTON = Button(image=None, pos=(250, 300), 
                            text_input="Volume Down", font=self.get_font(30), 
                            base_color="White", hovering_color="#9400D3")
            VOLUME_UP_BUTTON.changeColor(OPTIONS_MOUSE_POS)
            VOLUME_UP_BUTTON.update(self.screen)
            VOLUME_DOWN_BUTTON.changeColor(OPTIONS_MOUSE_POS)
            VOLUME_DOWN_BUTTON.update(self.screen)
            OPTIONS_BACK = Button(image=None, pos=(400, 500), 
                                text_input="BACK", font=self.get_font(30), base_color="White", hovering_color="#9400D3")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()
                        self.options()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if VOLUME_UP_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                            self.clickSound.play()
                            self.Tetris.increase_volume(0.1)
                    elif VOLUME_DOWN_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                            self.clickSound.play()
                            self.Tetris.decrease_volume(0.1)
            pygame.display.update()
    def level(self):
        while True:
            self.screen.blit(self.BG, (0, 0))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            
            EASY_BUTTON = Button(image=None, pos=(250, 200), 
                            text_input="EASY", font=self.get_font(30), 
                            base_color="White", hovering_color="#9400D3")
            MEDIUM_BUTTON = Button(image=None, pos=(250, 300), 
                            text_input="MEDIUM", font=self.get_font(30), 
                            base_color="White", hovering_color="#9400D3")
            HARD_BUTTON = Button(image=None, pos=(250, 400), 
                            text_input="HARD", font=self.get_font(30), 
                            base_color="White", hovering_color="#9400D3")
            
            OPTIONS_BACK = Button(image=None, pos=(400, 500), 
                                text_input="BACK", font=self.get_font(30), base_color="White", hovering_color="#9400D3")
            
            EASY_BUTTON.changeColor(OPTIONS_MOUSE_POS)
            EASY_BUTTON.update(self.screen)
            MEDIUM_BUTTON.changeColor(OPTIONS_MOUSE_POS)
            MEDIUM_BUTTON.update(self.screen)
            HARD_BUTTON.changeColor(OPTIONS_MOUSE_POS)
            HARD_BUTTON.update(self.screen)
            
            

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()
                        self.main_menu()
                    elif EASY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()
                        self.Tetris.levels = pygame.time.set_timer(self.Tetris.game_update, 400)
                        self.options()
                    elif MEDIUM_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()
                        self.Tetris.levels = pygame.time.set_timer(self.Tetris.game_update, 250)
                        self.options()
                    elif HARD_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()
                        self.Tetris.levels = pygame.time.set_timer(self.Tetris.game_update, 150)
                        self.options()
                pygame.display.update()
    def options(self):
        while True:
            
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.blit(self.BG, (0, 0))
            
            VOLUME = Button(image=None, pos=(250, 200), 
                            text_input="VOLUME", font=self.get_font(30), 
                            base_color="White", hovering_color="#9400D3")
            LEVEL= Button(image=None, pos=(250, 300), 
                            text_input="LEVEL", font=self.get_font(30), 
                            base_color="White", hovering_color="#9400D3")
            OPTIONS_BACK = Button(image=None, pos=(400, 500), 
                                text_input="BACK", font=self.get_font(30), base_color="White", hovering_color="#9400D3")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            VOLUME.changeColor(OPTIONS_MOUSE_POS)
            VOLUME.update(self.screen)
            LEVEL.changeColor(OPTIONS_MOUSE_POS)
            LEVEL.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()
                        self.main_menu()
                    if VOLUME.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()
                        self.volume()
                    if LEVEL.checkForInput(OPTIONS_MOUSE_POS):
                        self.clickSound.play()  
                        self.level() 
                pygame.display.update()
            
                
       
    def main_menu(self):
        while True:
            self.screen.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = pygame.image.load("Background/logo.png")
            MENU_RECT = MENU_TEXT.get_rect(center=(250, 100))

            PLAY_BUTTON = Button(image=None, pos=(250, 250), 
                                text_input="NEW GAME", font=self.get_font(40), base_color="#dc143c", hovering_color="#dcdcdc")
            OPTIONS_BUTTON = Button(image=None, pos=(250, 300), 
                                text_input="OPTIONS", font=self.get_font(40), base_color="#ff7f50", hovering_color="#dcdcdc")
            QUIT_BUTTON = Button(image=None, pos=(250, 350), 
                                text_input="QUIT", font=self.get_font(40), base_color="#b8860b", hovering_color="#dcdcdc")
            CONTINUE_BUTTON = Button(image=None, pos=(250, 200), 
                                    text_input="", font=self.get_font(40), base_color="#ff1493", hovering_color="#dcdcdc")
            if not self.checkGame:
                CONTINUE_BUTTON = Button(image=None, pos=(250, 200), 
                                    text_input="CONTINUE", font=self.get_font(40), base_color="green", hovering_color="white")
            self.screen.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON,CONTINUE_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS) and not self.checkGame:
                        self.clickSound.play()
                        self.play()
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.clickSound.play()
                        self.Tetris.resetgame()
                        self.checkGame = False
                        self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.clickSound.play()
                        self.options()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.clickSound.play()
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    def run(self):
            while True:
                self.main_menu()
                    
if __name__ == "__main__":
    Game1 = Menu()
    Game1.run()
        