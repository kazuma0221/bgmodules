from dataclasses import dataclass
from boardgame.rules import Rules
from boardgame.player import Player
from boardgame.dto import InputData

@dataclass
class Table:
    '''ゲーム卓。ゲームに必要なデータを保持する。
    Args:
        rules (Rules): ゲームのルール。
        players (list[Player]): ゲームのプレイヤーのlist。
        pieces (list): ゲームの内容物のlist。型は何でもよく、Pieceクラスに限らない。
        input_data (InputData): PRからAPへの入力DTO。
    '''
    rules: Rules
    players: list[Player]
    pieces: list
    input_data: InputData

# テスト
if __name__ == '__main__':
    # プレイヤーを作成
    from boardgame.player import makePlayers, PlayerType as PT
    players = makePlayers(types=[PT.HUMAN, PT.AI_RANDOM], names=['You', 'CPU'])

    # ルールを適当に作成
    class TestRules(Rules):
        def isPlayable(self, play, player, table):
            return True

    # コマを適当に作成
    from bgpieces.color import Color
    from bgpieces.piece import Piece
    pieces = [Piece(color=color) for color in Color.items()]

    # 本題：テーブルを作り、内容を確認
    print('---------')
    from boardgame.event_type import EventType as ev
    table = Table(rules=TestRules(), players=players, pieces=pieces, input_data=InputData())
    for elem in table.__dict__.items():
        print(elem)
    print('---------')