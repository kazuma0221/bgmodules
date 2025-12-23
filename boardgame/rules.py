from abc import ABC, abstractmethod

class Rules(ABC):
    '''ゲームのプレイ規則を定義する。'''
    @abstractmethod
    def isPlayable(self, play, player, table)->bool:
        '''プレイヤーの選んだ手が、着手可能かどうかを返す。
        :param any play: 着手。
        :param any player: 着手するプレイヤー。
        :param any table: ゲーム卓。'''
        pass