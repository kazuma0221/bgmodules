from abc import ABC, abstractmethod

class Rules(ABC):
    '''ゲームのプレイ規則を定義する抽象クラス。'''
    @abstractmethod
    def isPlayable(self, play, player, table)->bool:
        '''プレイヤーの選んだ手が、着手可能かどうかを返す抽象メソッド。
        Args:
            play (any): 着手の内容。
            player (any): 着手するプレイヤー。
            table (any): ゲーム卓。
        Returns:
            bool: 着手可能であればTrueを、そうでなければFalseを返すように実装する。'''
        pass