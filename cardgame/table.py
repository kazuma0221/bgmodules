import copy
from cardgame.rules import Rules
from playingcards.card import Card
from playingcards.deck import Deck
from cardgame.player import Player, makePlayers

class Table():
    '''ゲーム卓。ゲームに必要なデータを保持する。'''
    def __init__(self, inputData:dict, rules:Rules=Rules(), deck:Deck=Deck()):
        '''データを保持する変数を生成する。'''
        # 必須データ
        self.rules: Rules = rules
        self.deck: Deck = deck.shuffle()
        self.deck_backup = copy.deepcopy(self.deck)
        self.inputData: dict = inputData
        # 初期化
        self.players: list[Player] = makePlayers(types=inputData['player_types'], names=inputData['player_names'])
        self.event: dict = {}
        self.dealer: int = None
        self.turn: int = None
        self.playedCards: list[Card] = []
        self.scores: list[int] = [0] * len(self.players)
        self.totalScores: list[list[int]] = [[] for _ in self.players]

    def newDeck(self):
        '''元のデッキをコピーした新しいデッキを作る。戻り値はコピーしたデッキ。'''
        self.deck = copy.deepcopy(self.deck)
        return self.deck

# 単体テスト
if __name__ == '__main__':
    from cardgame.playertype import PlayerType as Type
    inputData = {'player_types': [Type.HUMAN, Type.AI_RANDOM],
              'player_names': ['You', 'CPU']}
    rules = Rules(handsize=10)
    table = Table(inputData=inputData, rules=rules)
    for elem in table.__dict__.items():
        print(elem)