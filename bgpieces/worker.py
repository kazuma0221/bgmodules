from enum import IntEnum
from bgpieces.piece import Piece
from bgpieces.color import Color

class WorkerSize(IntEnum):
    '''ワーカーの大小を定義する列挙型。'''
    BIG = 3
    MEDIUM = 2
    SMALL = 1

class Worker(Piece):
    '''ワーカーのクラス。色と大きさを持たせる。'''
    def __init__(self, color:Color, size:WorkerSize=WorkerSize.SMALL):
        super().__init__(color)
        self.size = size