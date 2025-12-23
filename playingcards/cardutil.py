from playingcards.card import Card
from playingcards.suit import Suit
from playingcards.rank import Rank

def makeCard(name:str)->Card:
    '''渡した2文字に該当するCardのリストを返す。1文字目はスート、2文字目はランク。
    スートはSHDCJ、ランクはAKQJT98765432（Tは10）。ジョーカーのランクは強い方がA、弱い方が2。
    一方または両方が小文字でも可。'''
    # 文字数チェック
    if len(name) != 2:
        raise ValueError(name)

    # スート
    s = name[0].upper()
    suit_dict = {'S': Suit.Spades, 'H': Suit.Hearts, 'D': Suit.Diamonds, 'C': Suit.Clubs, 'J': Suit.X}
    suit = suit_dict[s]

    # ランク
    r = name[1].upper()
    rank_dict = {'A': Rank.Ace, 'K': Rank.King, 'Q': Rank.Queen, 'J': Rank.Jack, 'T': Rank.Ten,
                '9': Rank.Nine, '8': Rank.Eight, '7': Rank.Seven, '6': Rank.Six, '5': Rank.Five,
                '4': Rank.Four, '3': Rank.Three, '2': Rank.Two}
    rank = rank_dict[r]

    # カードを作る
    return Card(rank=rank, suit=suit)

def makeHand(cards:list[str])->list[Card]:
    '''makeCard()の一括作成版。渡した文字列のリストに該当する手札を返す。
    各文字列の1文字目はスート、2文字目はランク。'''

    card_list = []
    for name in cards:
        # カードを作る
        card_list.append(makeCard(name))
    return card_list