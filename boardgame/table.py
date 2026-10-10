from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

from boardgame.player import Player
from boardgame.dto import InputData
if TYPE_CHECKING:
    from boardgame.rules.rules import BaseRules

@dataclass
class Table:
    '''ゲーム卓。ゲームに必要なデータを保持する。
    Args:
        rules (BaseRules): ゲームのルール。
        players (list[Player]): ゲームのプレイヤーのlist。
        pieces (list): ゲームの内容物のlist。型は何でもよく、Pieceクラスに限らない。
        input_data (InputData): PRからAPへの入力DTO。
    '''
    rules: BaseRules
    players: list[Player]
    pieces: list
    input_data: InputData

# テスト
if __name__ == '__main__':
    # プレイヤーを作成
    from boardgame.player import make_players, PlayerType as PT
    players = make_players(types=[PT.HUMAN, PT.AI_RANDOM], names=['You', 'CPU'])

    # ルールを適当に作成
    from boardgame.rules import BaseRules, BaseActionExecutor, BaseScoreCalculator, BaseTurnPostProcessor
    class MockActionExecutor(BaseActionExecutor):
        pass
    class MockScoreCalculator(BaseScoreCalculator):
        def calculate_score(self, player: object, table: object) -> int | float:
            pass
    class MockTurnPostProcessor(BaseTurnPostProcessor):
        def process(self, table: object):
            pass
    class Rules(BaseRules):
        def __init__(self):
            self._executor = MockActionExecutor()
            self._calculator = MockScoreCalculator()
            self._turn_post_processor = MockTurnPostProcessor()

    # コマを適当に作成
    from bgpieces.color import Color
    from bgpieces.piece import Piece
    pieces = [Piece(color=color) for color in Color.items()]

    # 本題：テーブルを作り、内容を確認
    print('---------')
    table = Table(rules=Rules(), players=players, pieces=pieces, input_data=InputData())
    for elem in table.__dict__.items():
        print(elem)
    print('---------')