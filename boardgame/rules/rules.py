from abc import ABC
from boardgame.player import Player
from boardgame.table import Table
from boardgame.rules.calculator import BaseScoreCalculator
from boardgame.rules.executor import BaseActionExecutor
from boardgame.rules.turn_post_processor import BaseTurnPostProcessor


class BaseRules(ABC):
    '''ゲームのプレイ規則を定義する抽象クラス（ファサード）。'''

    def __init__(self):
        self._executor = BaseActionExecutor()
        self._calculator = BaseScoreCalculator()
        self._turn_post_processor = BaseTurnPostProcessor()

    def is_playable(self, play: dict, player: Player, table: Table) -> bool:
        '''着手可能かどうかをエグゼキューターへ委譲する。'''
        if self._executor:
            return self._executor.is_playable(play, player, table)
        return False

    def apply_action(self, play: dict, player: Player, table: Table):
        '''アクション実行をエグゼキューターへ委譲する。'''
        if self._executor:
            return self._executor.execute(play, player, table)
        return None

    def calculate_score(self, player: Player, table: Table) -> int | float:
        '''得点計算を計算クラスへ委譲する。'''
        if self._calculator:
            return self._calculator.calculate_score(player, table)
        return 0

    def finalize_turn(self, table: Table) -> None:
        '''手番終了処理を後処理クラスへ委譲する。'''
        if self._turn_post_processor:
            self._turn_post_processor.process(table)