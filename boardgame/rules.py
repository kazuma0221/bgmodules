from abc import ABC, abstractmethod
from boardgame.player import Player
from boardgame.table import Table

class Rules(ABC):
    '''ゲームのプレイ規則を定義する抽象クラス。'''
    @abstractmethod
    def isPlayable(self, play, player: Player, table: Table)->bool:
        '''プレイヤーの選んだ手が、着手可能かどうかを返す抽象メソッド。
        Args:
            play (any): 着手の内容。
            player (Player): 着手するプレイヤー。
            table (Table): ゲーム卓。
        Returns:
            bool: 着手可能であればTrueを、そうでなければFalseを返すように実装する。'''
        raise NotImplementedError