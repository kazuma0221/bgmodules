import copy
from numpy import random

from playingcards.card import Card
from cardgame.playertype import PlayerType

def makePlayers(types:list[PlayerType], names:list[str], hands:list[list]=None):
    '''プレイヤータイプ、名前、手札のリストからPlayerオブジェクトのリストを作って返すユーティリティ関数。
    引数で受け取ったリストをzip()で展開するので、各リストの長さは同じであるのが望ましい。
    :param list types: プレイヤータイプのリスト。
    :param list names: 名前のリスト。
    :param list hand: 手札のリスト。指定しなければ空リストにする。'''
    if hands is None:
        hands = [[] for _ in types]
    return [Player(ptype=ptype, pname=name, hand=hand) for ptype, name, hand in zip(types, names, hands)]

class Player():
    '''カードゲームのプレイヤーを表すクラス。
    手札をリストで保持して操作を行う（リストのシンタックスシュガー）。
    ゲーム卓（Table）側でPlayerオブジェクトを作成するので、循環参照を避けるため
    このファイルにTableクラスをimportしないこと。'''
    def __init__(self, ptype:PlayerType=PlayerType.AI_RANDOM, pname:str='Default', hand:list=[]):
        '''プレイヤータイプ、手札、名前をセットする。'''
        self.ptype: PlayerType = ptype
        self.pname: str = pname
        self.hand: list[Card] = hand
        self.pointPile: list[Card] = []
        self.rng = random.default_rng()

    def setType(self, ptype:PlayerType):
        '''プレイヤータイプのセッター。0が人間、1がコンピュータ。'''
        self.ptype = ptype

    def getType(self):
        '''プレイヤータイプのゲッター。0が人間、1がコンピュータ。'''
        return self.ptype

    def getHand(self)->list[Card]:
        '''全手札のゲッター。手札からは抜かず、単に参照を返す。'''
        return self.hand

    def getCard(self, i:int):
        '''手札1枚のゲッター。手札からは抜かず、単に参照を返す。'''
        return self.hand[i]

    def setHand(self, hand:list[Card]):
        '''手札のリストをセットする。'''
        self.hand = hand

    def getpointPile(self)->list[Card]:
        '''全獲得札のゲッター。'''
        return self.pointPile

    def getPointCard(self, i:int):
        '''獲得札1枚のゲッター。'''
        return self.pointPile[i]

    def setPointCard(self, card:Card):
        '''獲得札1枚をセットする。'''
        self.pointPile.append(card)

    def sort(self, reverse:bool=True):
        '''手札のリストをソートする。ソートした手札を返す。'''
        self.hand.sort(reverse=reverse)

    def addCard(self, card:Card):
        '''カードを1枚、手札の末尾に追加する。'''
        self.hand.append(card)

    def getIdxInHand(self, card:Card, default:int=-1)->int:
        '''指定したカードの手札のインデックスを返す。なければデフォルト(-1)を返す。
        :param Card card: 手札から探すカード。
        :param int default: カードがなかったときに返す値。設定しなければ-1。'''
        if card in self.hand:
            return self.hand.index(card)
        return default

    def copyPlayable(self, table):
        '''プレイ可能な手札のコピーを返す。'''
        copylist = copy.deepcopy(self.hand)
        return [card for i, card in enumerate(copylist) if table.rules.isPlayable(table.playedCards, copylist, i)]

    def playCard(self, c)->tuple[int, Card]:
        '''選んだカードを1枚プレイする。手札から抜いて(インデックス, カード)のタプルを返す。
        intを設定すれば順番指定、カードを入れたら手札の最初に該当するものを選ぶ。
        存在しないものを指定するとNoneを返す。
        :param Any i: intを指定すればそのインデックスのカードを抜く。カード自体を指定すれば同じオブジェクトの有無を調べて、あれば返す。'''
        if isinstance(c, int):
            return (c, self.hand.pop(c))
        if c in self.hand:
            return (self.hand.index(c), self.hand.pop(self.hand.index(c)))
        return None

    def clear(self):
        '''手札と獲得札のリストをクリアする。'''
        del self.hand[:]
        del self.pointPile[:]

    def chooseCard(self, table):
        '''ルールを参照し、プレイ可能なカードを手札からランダムに選び、そのカードを返す。
        デフォルトではトリックテイキングのルールに従って判定する。
        選び方を別途実装する場合、このメソッドを上書きする。'''
        playable_list = [card for i, card in enumerate(self.hand) if table.rules.isPlayable(played=table.playedCards, hand=self.hand, choice=i)]
        return self.rng.choice(playable_list)

# テスト用
if __name__ == '__main__':
    from playingcards.deck import Deck
    from cardgame.ttrules import TTRules
    from cardgame import inputData
    from cardgame.table import Table

    # デッキとプレイヤーを用意
    deck = Deck().shuffle()
    player = Player(PlayerType.AI_RANDOM)

    # 手札一覧を表示
    player.setHand([deck.pick() for _ in range(10)])
    print('--- Player Hands:')
    player.sort()
    print([card.string() for card in player.getHand()])

    # 指定したカードの手札のインデクスが正しいことの確認
    print('\n--- card offset 3:')
    chosen_card = player.getCard(3)
    print(f'{chosen_card.string()}: {str(player.getIdxInHand(chosen_card))}')

    # テーブルを用意し、カードをデッキから適当に2枚プレイ
    print('\n--- On the table:')
    table = Table(inputData=inputData.makeTestData(), rules=TTRules(handsize=2))
    table.playedCards = [deck.pick() for _ in range(2)]
    print([card.string() for card in table.playedCards])

    # 手札を見て、プレイ可能なカードを抜き出す
    print('\n--- Playable Cards:')
    print([card.string() for card in player.copyPlayable(table)])

    # 1枚選ぶ
    print('\n--- Method execution:')
    print(player.chooseCard(table).string())