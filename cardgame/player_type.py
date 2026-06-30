from enum import IntEnum

class PlayerType(IntEnum):
    '''プレイヤーの種類を表す整数列挙型。'''
    HUMAN = 0
    AI_RANDOM = 1
    AI_MODEST = 2
    AI_LOSE = 3