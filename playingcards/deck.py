from numpy import random
from playingcards.rank import Rank
from playingcards.suit import Suit
from playingcards.card import Card

class Deck():
    '''トランプゲームのデッキ（山札）を表すクラス。指定したランク・スートに基づく山札を生成し、各種操作を行う。'''
    deck = []

    def __init__(self):
        '''デッキを作成し、乱数ジェネレータを初期化する。'''
        self.create()
        self.random_generator = random.default_rng()

    def create(self, joker:bool=False):
        '''ランク×スートの総当たりデッキを作成する。'''
        ranks = [rank for rank in Rank]
        suits = [suit for suit in Suit if suit is not Suit.X]
        self.deck = [Card(rank, suit) for rank in ranks for suit in suits]
        if joker:
            self.deck.append(Card(Rank.Ace, Suit.X))
            self.deck.append(Card(Rank.Two, Suit.X))

    def __setitem__(self, key, value):
        '''添字アクセス用のセッター。'''
        self.deck[key] = value

    def __getitem__(self, key):
        '''添字アクセス用のゲッター。'''
        return self.deck[key]

    def __len__(self):
        '''len()関数用のゲッター。'''
        return len(self.deck)

    def shuffle(self):
        '''山札をシャッフルし、山札自体を返す。'''
        self.random_generator.shuffle(self.deck)
        return self

    def draw(self, howmany:int=1)->list[Card]:
        '''山札の上から指定した枚数を抜いたリストを返す。足りないときは、抜けるだけ返す。'''
        ret = []
        if howmany < 1:
            return ret
        for _ in range(howmany):
            if len(self.deck) < 1:
                break
            ret.append(self.deck.pop(0))
        return ret

    def pick(self)->Card:
        '''山札の上から1枚抜いて返す。'''
        return self.deck.pop(0)

    def add(self, card:Card):
        '''山札の下に1枚追加する。'''
        self.deck.append(card)
        return self

    def extend(self, cards:list[Card]):
        '''山札にカードのリストを追加する。'''
        self.deck.extend(cards)
        return self

    def size(self)->int:
        '''山札の枚数を返す。'''
        return len(self.deck)

# テスト用
if __name__ == '__main__':
    deck = Deck(joker=True).shuffle()
    handSize = int(deck.size() / 4)
    hand = [deck.pick() for i in range(handSize)]
    hand.sort()
    print(', '.join([card.string() for card in hand]))