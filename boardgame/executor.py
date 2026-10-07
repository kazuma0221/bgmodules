from abc import ABC
from boardgame.action import BaseAction


class BaseActionExecutor(ABC):
    '''アクションコマンド群の登録・実行統括を行う抽象基底クラス。'''

    def __init__(self):
        self._actions: dict[str, BaseAction] = {}

    def register_action(self, action_type: str, action: BaseAction):
        '''アクション種別に応じたCommandインスタンスを登録する。

        Args:
            action_type (str): アクション種別を表すキー。
            action (BaseAction): 対応するアクションCommandインスタンス。
        '''
        self._actions[action_type] = action

    def is_playable(self, play: dict, player: object, table: object) -> bool:
        '''指定されたアクションが実行可能かどうかを判定する。

        Args:
            play (dict): アクションパラメータ。
            player (object): アクションを実行するプレイヤー。
            table (object): 現在のゲーム卓。

        Returns:
            bool: 実行可能であればTrue。
        '''
        action_type = play.get('action_type')
        if not action_type or action_type not in self._actions:
            return False
        return self._actions[action_type].is_playable(play, player, table)

    def execute(self, play: dict, player: object, table: object):
        '''指定されたアクションを実行する。（未定義のアクションは辞書_actionsのKeyErrorになる。）

        Args:
            play (dict): アクションパラメータ。
            player (object): アクションを実行するプレイヤー。
            table (object): 現在のゲーム卓。

        Returns:
            任意。指定されたアクションの戻り値をそのまま返す。
        '''
        action_type = play.get('action_type')
        return self._actions[action_type].execute(play, player, table)