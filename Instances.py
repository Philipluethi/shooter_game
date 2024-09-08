
import pygame
from Constants import *
from Block import BLOCK
from Bullet import BULLET
from Player import PLAYER
from Effects import *
from Interface import INTERFACE


player_1 = PLAYER(1, 500, 0)
player_2 = PLAYER(2, 200, 0)
blocks = []
items = [
    ITEM_BOX()
        ]
interface = INTERFACE()