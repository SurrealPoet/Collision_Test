import pygame as pg
from pygame.math import Vector2

pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color(30, 90, 0)

# You need surfaces with an alpha channel to
# create masks, therefore pass `pg.SRCALPHA`.
REDGOAL = pg.Surface((90, 150), pg.SRCALPHA)
REDGOAL.fill((255, 0, 0))
redgoal_rect = REDGOAL.get_rect(topleft=(100, 200))
redgoal_mask = pg.mask.from_surface(REDGOAL)

BALL = pg.Surface((30, 30), pg.SRCALPHA)
pg.draw.circle(BALL, [250, 250, 250], [15, 15], 15)
# Ball variables.
ball_pos = Vector2(275, 200)
ballrect = BALL.get_rect(center=ball_pos)
ball_vel = Vector2(0, 0)
ball_mask = pg.mask.from_surface(BALL)

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                ball_vel.x = -7
            elif event.key == pg.K_d:
                ball_vel.x = 8
            elif event.key == pg.K_w:
                ball_vel.y = -3
            elif event.key == pg.K_s:
                ball_vel.y = 5

    ball_vel *= .94  # Friction.
    ball_pos += ball_vel
    ballrect.center = ball_pos

    if ballrect.top < 0 and ball_vel.y < 0:
        ball_vel.y *= -1
    elif ballrect.bottom > screen.get_height() and ball_vel.y > 0:
        ball_vel.y *= -1
    if ballrect.left < 0 and ball_vel.x < 0:
        ball_vel.x *= -1
    elif ballrect.right > screen.get_width() and ball_vel.x > 0:
        ball_vel.x *= -1

    # Rect collision.
    # if ballrect.colliderect(redgoal_rect):
    #     print('goal!')

    # Calculate the offset between the objects.
    offset = redgoal_rect[0] - ballrect[0], redgoal_rect[1] - ballrect[1]
    # Pass the offset to the `overlap` method. If the masks collide,
    # overlap will return a single point, otherwise `None`.
    overlap = ball_mask.overlap(redgoal_mask, offset)

    if overlap:
        print('goal!')

    screen.fill(BG_COLOR)
    screen.blit(BALL, ballrect)
    screen.blit(REDGOAL, redgoal_rect)
    pg.display.flip()
    clock.tick(60)

pg.quit()
