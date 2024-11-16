import sys
import pygame
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)
game_score = 0

# size of screen
screen_width, screen_height = 800, 600
screen_fill_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

# name of game
pygame.display.set_caption("Alien")

# fighter
FIGHTER_STEP = 5
fighter_image = pygame.image.load('../images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x = (screen_width - fighter_width) / 2
fighter_y = (screen_height - fighter_height)
fighter_is_moving_left = False
fighter_is_moving_right = False

# alien
alien_image = pygame.image.load('../images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x = randint(0, screen_width - alien_width)
alien_y = 0
alien_step = 0.5

# ball
ball_image = pygame.image.load('../images/ball.png')
ball_width, ball_height = ball_image.get_size()
ball_x, ball_y = 0, 0
BALL_STEP = 10
ball_was_fire = False

game_is_running = True
while game_is_running:
    for event in pygame.event.get():
        # exit
        if event.type == pygame.QUIT:
            sys.exit()

        # KEYDOWN
        if event.type == pygame.KEYDOWN:
            # For fighter
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True

            # For
            if event.key == pygame.K_UP:
                ball_was_fire = True
                ball_x = fighter_x + fighter_height / 2
                ball_y = fighter_y - ball_height

        # KEYUP
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    # moving_fighter
    if fighter_is_moving_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_moving_right and fighter_x <= screen_width - FIGHTER_STEP - fighter_width:
        fighter_x += FIGHTER_STEP

    # moving_ball
    if ball_was_fire:
        ball_y -= BALL_STEP
    if ball_y + ball_height <= 0 and ball_was_fire:
        ball_was_fire = False

    # moving_alien
    alien_y += alien_step

    # tacksture
    screen.fill(screen_fill_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))

    if ball_was_fire:
        screen.blit(ball_image, (ball_x, ball_y))

    game_score_text = game_font.render(f'Your score is: {game_score}', True, 'white')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        alien_y = 0
        game_is_running = False

    if ball_was_fire and \
            (alien_x < ball_x < alien_x + alien_width or
             alien_x < ball_x + ball_width < alien_x + alien_width) \
            and ball_y <= alien_y + alien_height:
        ball_was_fire = False
        alien_x = randint(0, screen_width - alien_width)
        alien_y = 0
        game_score += 1
        alien_step *= 1.1

game_over_text = game_font.render('GAME OVER', True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(2500)
pygame.quit()
