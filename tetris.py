import pygame, sys
# from grid import Grid
from blocks import *
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)

score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)


#clock set khung hình cho game 
clock = pygame.time.Clock()

#màn hình
screen = pygame.display.set_mode((500, 620))

#color màn hình


#tiêu đề
pygame.display.set_caption('Tetris')

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

#cái lưới 
# game_grid = Grid()
# # game_grid.grid[0][0] = 1
# # game_grid.grid[3][5] = 4
# # game_grid.grid[17][8] = 7

 

# # game_grid.print_grid()
# block = IBlock() 
game = Game()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over =False
                game.reset()
            if event.key == pygame.K_a and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_d and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_s and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_w and game.game_over == False:
                game.rotate() 
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.gray) #màu màn hình màu xanh
    screen.blit(score_surface, (365, 20, 50, 50))# chữ score
    screen.blit(next_surface,(375, 180, 50, 50))# chữ next
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))#tuple nè  chữ game over hiện ra khi thua

    pygame.draw.rect(screen, Colors.light_blue, score_rect,0 ,10)
    screen.blit (score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    # game_grid.draw(screen)
    # block.draw(screen)
    game.draw(screen) ##########################
   
    pygame.display.update()
    clock.tick(60) #tức là 60 khung hình sẽ chạy trên 1 giây 
    