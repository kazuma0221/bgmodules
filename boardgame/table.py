from dataclasses import dataclass, field
from boardgame.rules import Rules
from boardgame.player import Player

@dataclass
class Table:
    '''ゲーム卓。ゲームに必要なデータを保持する。
    :param Rules rules: ゲームのルール。
    :param list[Players] players: ゲームのプレイヤーのlist。
    :param list pieces: ゲームの内容物のlist。型は何でもよく、Pieceクラスに限らない。
    :param dict inputData: PRからAPに入力するデータの辞書。作成時は空でもよい。
    :param dict event: APからPRに出力するデータの辞書。作成時は空にすることを推奨する。'''
    rules: Rules
    players: list[Player]
    pieces: list
    inputData: dict = field(default_factory=dict)
    event: dict = field(default_factory=dict)

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
    table = Table(rules=TestRules(), players=players, pieces=pieces)
    for elem in table.__dict__.items():
        print(elem)
    print('---------')