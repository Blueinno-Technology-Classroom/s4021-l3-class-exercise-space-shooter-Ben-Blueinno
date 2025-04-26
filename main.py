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

enemy_ship = [
    'enemyblack1',
    'enemyblack2',
    'enemyblack3',
    'enemyblack4',
    'enemyblack5',
    'enemyblue1',
    'enemyblue2',
    'enemyblue3',
    'enemyblue4',
    'enemyblue5',
    'enemygreen1',
    'enemygreen2',
    'enemygreen3',
    'enemygreen4',
    'enemygreen5',
    'enemyred1',
    'enemyred2',
    'enemyred3',
    'enemyred4',
    'enemyred5',
]

player.hp = 100


def update():

    if random.randint(0, 100) < 5:
        enemy = Actor(random.choice(enemy_ship))
        enemy.x = random.randint(0, WIDTH)
        enemy.y = random.randint(0, 100)
        enemy.point_towards(player)
        enemies.append(enemy)

    for enemy in enemies:
        if random.randint(0, 100) < 1:
            laser = Actor('laserred01')
            laser.pos = enemy.pos
            laser.point_towards(player)
            enemy_lasers.append(laser)

    if keyboard.space:
        laser = Actor('laserblue16')
        laser.pos = player.pos
        if len(enemies) > 0:
            laser.point_towards(random.choice(enemies))
        else:
            laser.angle = 90
        player_lasers.append(laser)

    for laser in player_lasers:
        laser.move_forward(5)
        if laser.bottom < 0:
            player_lasers.remove(laser)
        else:
            for enemy in enemies:
                if laser.collide_pixel(enemy):
                    player_lasers.remove(laser)
                    enemies.remove(enemy)
                    break

    for laser in enemy_lasers:
        laser.move_forward(5)  # move the laser
        if laser.top > HEIGHT:  # go out of screen
            enemy_lasers.remove(laser)
        else:
            if player.collide_pixel(laser):  # collided with player
                enemy_lasers.remove(laser)
                player.hp = player.hp - 1

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
    for enemy in enemies:
        enemy.draw()
    for laser in player_lasers:
        laser.draw()
    for laser in enemy_lasers:
        laser.draw()
    player.draw()
    screen.draw.filled_rect(Rect((0, 0), (WIDTH*player.hp/100, 20)), 'green')


pgzrun.go()
