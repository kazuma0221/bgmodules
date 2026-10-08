from abc import ABC, abstractmethod


class BaseAction(ABC):
    '''ボードゲームにおける個別アクションの判定と実行を定義する抽象基底クラス。'''

    @abstractmethod
    def is_playable(self, play: dict, player: object, table: object) -> bool:
        '''指定されたアクションが実行可能かどうかを判定する。

        Args:
            play (dict): アクションパラメータ。
            player (object): アクションを実行するプレイヤー。
            table (object): 現在のゲーム卓。

        Returns:
            bool: 実行可能であればTrue。
        '''
        pass

    @abstractmethod
    def execute(self, play: dict, player: object, table: object):
        '''アクションを実行し、ゲーム状態を更新する。

        Args:
            play (dict): アクションパラメータ。
            player (object): アクションを実行するプレイヤー。
            table (object): 現在のゲーム卓。
        '''
        pass