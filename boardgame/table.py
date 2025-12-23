from boardgame.rules import Rules
from boardgame.player import Player

class Table():
    '''ゲーム卓。ゲームに必要なデータを保持する。
    :param Rules rules: ゲームのルール。
    :param list[Players] players: ゲームのプレイヤーのlist。
    :param list pieces: ゲームの内容物のlist。型は何でもよく、Pieceクラスに限らない。'''
    def __init__(self, rules:Rules, players:list[Player], pieces:list, inputData:dict={}):
        self.rules: Rules = rules
        self.players: list[Player] = players
        self.pieces: list = pieces
        self.inputData: dict = inputData
        self.event: dict = {}

# テスト
if __name__ == '__main__':
    # プレイヤーを作成
    from boardgame.player import makePlayers
    from boardgame.player import PlayerType as Type
    players = makePlayers(types=[Type.HUMAN, Type.AI_RANDOM], names=['You', 'CPU'])

    # ルールを適当に作成
    class TestRules(Rules):
        def isPlayable(self, play, player, table):
            return True

    # コマを適当に作成
    from bgpieces.color import Color
    from bgpieces.piece import Piece
    pieces = []
    for color in Color.items():
        pieces.append(Piece(color=color))

    table = Table(rules=TestRules(), players=players, pieces=pieces)
    for elem in table.__dict__.items():
        print(elem)