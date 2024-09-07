import pygame
import sys
from game import Game
from colors import Colors
class TetrisGame:
    def __init__(self):
        pygame.init()
        self.paused = False
        self.controls_enabled = True
        self.pause_font = pygame.font.Font("Font/Atop-R99O3.ttf", 25)
        self.pause_text1 = self.pause_font.render("Press ESC", True, Colors.light)
        self.pause_text2 = self.pause_font.render("to continue", True, Colors.light)
        self.title_font = pygame.font.Font("Font/Atop-R99O3.ttf", 25)
        self.score_surface = self.title_font.render("Score", True, Colors.light)
        self.next_surface = self.title_font.render("Next", True, Colors.light)
        self.game_over_surface = self.title_font.render("GAME OVER", True, Colors.light)
        self.annouce_restart1 = self.title_font.render("Press SPACE", True, Colors.light)
        self.annouce_restart2 = self.title_font.render("to Reset", True, Colors.light)

        self.score_rect = pygame.Rect(320, 55, 170, 60)
        self.next_rect = pygame.Rect(320, 205, 170, 170)
        self.screen = pygame.display.set_mode((500, 620))
        pygame.display.set_caption("Tetris Game")
        
        self.soundtrack = pygame.mixer.Sound(f'sound/bgm.mp3')
        self.soundtrack.set_volume(0.4)
        self.soundtrack.play(-1)
        self.clock = pygame.time.Clock()
        self.game = Game()
        self.game_update = pygame.USEREVENT
        
        self.levels = pygame.time.set_timer(self.game_update, 300)
        self.status = True
        
        self.checkMenu = True
        
    def increase_volume(self, amount):
        current_volume = self.soundtrack.get_volume()
        new_volume = min(1.0, current_volume + amount)
        self.soundtrack.set_volume(new_volume)

    def decrease_volume(self, amount):
        current_volume = self.soundtrack.get_volume()
        new_volume = max(0.0, current_volume - amount)
        self.soundtrack.set_volume(new_volume)
    def resetgame(self):
        self.game.reset()
        self.game.game_over = False
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not self.game.game_over:
                    self.game.move_left()
                elif event.key == pygame.K_RIGHT and not self.game.game_over:
                    self.game.move_right()
                elif event.key == pygame.K_DOWN and not self.game.game_over:
                    self.game.move_down()
                    self.game.update_score(0, 1)
                elif event.key == pygame.K_SPACE and not self.game.game_over:
                    self.game.drop()
                    self.game.update_score(0, 10)
                elif event.key == pygame.K_UP and not self.game.game_over:
                    self.game.rotate()
                elif event.key == pygame.K_ESCAPE and not self.game.game_over:
                    self.checkMenu = False
                elif event.key == pygame.K_SPACE and self.game.game_over:
                    self.resetgame()
            elif event.type == self.game_update and not self.game.game_over:
                self.game.move_down()
    
    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            pygame.mixer.music.pause()
            pygame.time.set_timer(self.game_update, 0) 
        else:
            pygame.mixer.music.unpause()
            pygame.time.set_timer(self.game_update, 300)
            self.controls_enabled = True

    
    def draw(self):
        score_value_surface = self.title_font.render(str(self.game.score), True, Colors.light)
        self.screen.fill(Colors.dark_blue)
        self.screen.blit(self.score_surface, (365, 20, 50, 30))
        self.screen.blit(self.next_surface, (375, 170, 50 ,50))
        pygame.draw.rect(self.screen, Colors.light_blue, self.score_rect, 0, 10)
        pygame.draw.rect(self.screen, Colors.light_blue, self.next_rect, 0, 10)
        self.screen.blit(score_value_surface, score_value_surface.get_rect(centerx=self.score_rect.centerx, centery=self.score_rect.centery))
        if self.paused:
            self.screen.blit(self.pause_text1, (340, 450, 50, 50))
            self.screen.blit(self.pause_text2, (330, 500, 100, 30))
        if self.game.game_over:
            self.screen.blit(self.game_over_surface, (335, 450, 50, 50))
            self.screen.blit(self.annouce_restart1, (320, 500, 100, 30))
            self.screen.blit(self.annouce_restart2, (350, 540, 90, 30))
        self.game.draw(self.screen)
        pygame.display.update()