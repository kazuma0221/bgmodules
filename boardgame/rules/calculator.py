from abc import ABC, abstractmethod


class BaseScoreCalculator(ABC):
    '''得点計算を行う抽象基底クラス。'''

    @abstractmethod
    def calculate_score(self, player: object, table: object) -> int | float:
        '''プレイヤーの得点を計算して返す。

        Args:
            player (object): 対象のプレイヤー。
            table (object): 現在のゲーム卓。

        Returns:
            int | float: 計算された得点。
        '''
        pass