import random

import pgzrun

from pgzhelper import *

WIDTH = 1024
HEIGHT = 768

player = Actor("playership3_blue")
player.bottom = HEIGHT
player.x = WIDTH / 2

enemies = []
player_lasers = []
enemy_lasers = []


def update():
    if keyboard.a:
        player.x = player.x - 5
    if keyboard.LEFT:
        player.x = player.x - 5
    if keyboard.d:
        player.x = player.x + 5
    if keyboard.RIGHT:
        player.x = player.x + 5
    if keyboard.w:
        player.y -= 5
    if keyboard.UP:
        player.y -= 5
    if keyboard.s:
        player.y += 5
    if keyboard.DOWN:
        player.y += 5

    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH


def draw():
    screen.clear()
    player.draw()


pgzrun.go()
