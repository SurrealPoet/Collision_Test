import sys

import pygame as pg
from pygame.math import Vector2


def something_happens(rect1, rect2, mask_test):
    if pg.rect.Rect.colliderect(rect1, rect2):
        print("something_happens")
        return mask_test


class Test:
    def __init__(self):
        pg.init()
        self.window = pg.display.set_mode((1280, 736))
        self.mouse_position = Vector2()
        self.running = True
        self.clock = pg.time.Clock()

    def process_inputs(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    pg.quit()
                    sys.exit()

    def main(self):
        while self.running:
            self.process_inputs()
            self.window.fill((0, 0, 0))
            mx, my = pg.mouse.get_pos()
            circle = pg.Surface((200, 200), pg.SRCALPHA)
            pg.draw.circle(circle, (0, 255, 0), (100, 100), 100)
            # circle is located at the origin in the top left but circle_rect allows us to use
            # keywords to relocate Surface
            circle_rect = circle.get_rect(topleft=(400, 400))
            # .blit returns a rectangle
            self.window.blit(circle, circle_rect)
            circle_mask = pg.mask.from_surface(circle)
            rectangle = pg.Surface((80, 80), pg.SRCALPHA)
            pg.draw.rect(rectangle, (255, 0, 0), (0, 0, 40, 40))
            rect_image = self.window.blit(rectangle, (mx, my))
            rectangle_mask = pg.mask.from_surface(rectangle)
            offset = mx - circle_rect.topleft[0], my - circle_rect.topleft[1]
            mask_test = circle_mask.overlap(rectangle_mask, offset)
            # mask_test = pg.mask.Mask.overlap(circle_mask, rectangle_mask, offset)
            if something_happens(circle_rect, rect_image, mask_test):
                # Draw circle bigger than Surface to show that only surface is filled and the rest is not drawn
                pg.draw.circle(circle, (0, 0, 255), (100, 100), 500)
                self.window.blit(circle, circle_rect)
            pg.display.update()
            self.clock.tick(60)


Test().main()
