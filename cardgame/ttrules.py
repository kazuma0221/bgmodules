from playingcards.card import Card
from cardgame.rules import Rules

class TTRules(Rules):
    '''トリックテイキングのトリック勝敗を定義する。指定した切札カードのスートを用いて判定する。
    切札はセッターでカードを指定し、ノートランプはゲッターがNoneを返す。'''
    def __init__(self, handsize:int=0, trump:Card=None):
        '''手札枚数、切札を設定する。'''
        self.handsize = handsize
        self.trump = trump

    def whoWins(self, played:list[Card]):
        '''トリックに勝ったカードのインデックスを返す。
        :param list[Card] played: トリックにプレイされたカードのリスト。'''
        winner = played[0]
        for card in played:
            # ウィナーとスートが一致して、かつランクがより高ければ勝ち
            if (card.getSuit() == winner.getSuit()) and (card.getRank().value > winner.getRank().value):
                winner = card
            # 切札がある場合、ウィナーが切札でなく、かつこのカードが切札でも勝ち
            elif (self.trump is not None) \
                    and (winner.getSuit() != self.trump.getSuit()) \
                    and (card.getSuit() == self.trump.getSuit()):
                winner = card
        return played.index(winner)

# テスト用
if __name__ == '__main__':
    from playingcards.deck import Deck
    from playingcards import cardutil

    # 山札、ルール、切札を作成
    deck = Deck().shuffle()
    rulebook = TTRules()
    rulebook.setTrump(deck.pick())
    print('---')

    # マストフォローの確認
    played = [deck.pick() for _ in range(2)]
    hand = [deck.pick() for _ in range(7)]
    print(f'played: {", ".join([card.string() for card in played])}')
    print(f'hand: {", ".join([card.string() for card in hand])}')
    for i, card in enumerate(hand):
        print(f'{card.string()} is {("" if rulebook.isPlayable(played, hand, i) else "not ")}playable.')
    print('---')

    # 誰が勝つかの確認
    print(f'Trump suit is {rulebook.getTrump().getSuit().getMark()}')
    played = [deck.pick() for _ in range(4)]
    print('played: ' + ', '.join([card.string() for card in played]))
    print(str(rulebook.whoWins(played)) + ' wins.')

    # 任意の組合せで再テスト
    played = cardutil.makeHand(['SJ', 'S7', 'HA', 'SK'])
    print('played: ' + ', '.join([card.string() for card in played]))
    print(str(rulebook.whoWins(played)) + ' wins.')