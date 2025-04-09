import pygame as pg


coroa_img = pg.image.load("crown.png")
coroa_img = pg.transform.scale(coroa_img, (30, 30))

apple_img = pg.image.load("apple.png")
apple_img = pg.transform.scale(apple_img, (30, 30))

hole_img = pg.image.load("hole.png")
hole_img = pg.transform.scale(hole_img, (30, 30))

bush_img = pg.image.load("bush.png")
bush_img = pg.transform.scale(bush_img, (30, 30))

snake_head_img = pg.image.load("snake_head.png")
snake_head_img = pg.transform.scale(snake_head_img, (30, 30))

snake_body_img = pg.image.load("snake_body.png")
snake_body_img = pg.transform.scale(snake_body_img, (30, 30))

plano_img = pg.image.load("plano.png")
plano_img = pg.transform.scale(plano_img, (30, 30))