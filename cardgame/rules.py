from playingcards.card import Card

class Rules:
    '''ゲームのプレイ規則を定義する。'''
    def __init__(self, handsize:int=0):
        '''手札枚数を設定する。'''
        self.handsize = handsize

    def setHandSize(self, handsize:int):
        '''手札枚数を設定する。'''
        self.handsize = handsize

    def getHandSize(self):
        '''手札枚数を取得する。'''
        return self.handsize

    def setTrump(self, card:Card):
        '''切札指定のカードを設定する。'''
        self.trump = card

    def getTrump(self):
        '''切札指定のカードを取得する。'''
        return self.trump

    def isPlayable(self, played:list[Card], hand:list[Card], choice:int)->bool:
        '''渡された場札、手札、選んだカードから、そのカードが出せるかどうかを判定する。
        このクラスの実装はトリックテイキングゲームのマストフォローで、ゲーム実装に応じてこのメソッドをオーバーライドする。
        :param list[Card] played: 場にプレイされているカード一覧。
        :param list[Card] hand: 手札のカード一覧。
        :param int i: 手札から選ぶカード。'''
        # 場が空なら、何でもOK
        if len(played) < 1:
            return True
        # リードスートを取得
        leadsuit = played[0].getSuit()
        # リードスートが手札にあればそれを選んでいること、なければ何でもOK
        if leadsuit in [card.getSuit() for card in hand]:
            return hand[choice].getSuit() == leadsuit
        else:
            return True

# テスト用
if __name__ == '__main__':
    from playingcards.deck import Deck

    # 山札とルールを作成
    deck = Deck().shuffle()
    hand = [deck.pick() for _ in range(7)]
    rules = Rules(handsize=len(hand))

    # 手札の確認
    print('---')
    print('Your hand: ' + ', '.join([card.string() for card in hand]))
    for i, card in enumerate(hand):
        print(f'{card.string()} is {"" if rules.isPlayable(hand, i) else "not "}playable.')
    print('---')