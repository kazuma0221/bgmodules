from enum import Enum
from playingcards.card import Card

class Name(Enum):
    StraightFlush = 'STRAIGHT FLUSH'
    FourOfAKind = 'FOUR OF A KIND'
    FullHouse = 'FULL HOUSE'
    Flush = 'FLUSH'
    Straight = 'STRAIGHT'
    ThreeOfAKind = 'THREE OF A KIND'
    TwoPairs = 'TWO PAIRS'
    OnePair = 'ONE PAIR'
    HighCard = 'HIGH CARD'

def getHandName(row:list[Card])->Name:
    '''カード列のポーカー役を判定する。'''

    # フラッシュ
    isFlush = False
    hand = sorted(row, reverse=True)
    for i, card in enumerate(hand):
        if len(hand) < 5:
            break
        elif i == 0:
            suit = card.suit
        elif card.suit != suit:
            break
    else:
        isFlush = True

    # ストレート
    isStraight = False
    hand = sorted(row, key=lambda card: card.rank, reverse=True)
    rank = 0
    for i, card in enumerate(hand):
        if len(hand) < 5:
            break
        elif (i == 0) or (card.rank == rank - 1) or (rank == 14 and card.rank == 5):
            rank = card.rank
        else:
            break
    else:
        isStraight = True

    # ストフラ／フラッシュ／ストレート
    if isFlush and isStraight:
        return Name.StraightFlush
    elif isFlush:
        return Name.Flush
    elif isStraight:
        return Name.Straight

    # スリーカード（チェックのみ）／フォーカード
    equal_count = 1
    rank_of_three = 0
    isThreeOfAKind = False
    for i, card in enumerate(hand):
        if i == 0:
            rank = card.rank
        elif card.rank == rank:
            equal_count += 1
            if equal_count == 4:
                return Name.FourOfAKind
            elif equal_count == 3:
                isThreeOfAKind = True
                rank_of_three = rank
        else:
            equal_count = 1
            rank = card.rank

    # フルハウス／スリーカード／ツーペア／ワンペア
    pair_count = 0
    for i, card in enumerate(hand):
        if card.rank == rank_of_three:
            continue
        elif i == 0:
            rank = card.rank
        elif card.rank == rank:
            pair_count += 1
            if isThreeOfAKind:
                return Name.FullHouse
        else:
            rank = card.rank
    if pair_count == 2:
        return Name.TwoPairs
    elif pair_count == 1 and not isThreeOfAKind:
        return Name.OnePair
    elif isThreeOfAKind:
        return Name.ThreeOfAKind
    # それ以外はハイカード
    return Name.HighCard

if __name__ == '__main__':
    # テストケース
    from playingcards.cardutil import makeHand
    testcases = [
        makeHand(['CT', 'CK', 'CQ', 'CJ', 'CA']),   # ストフラ（AKQJT）
        makeHand(['H3', 'HA', 'H4', 'H2', 'H5']),   # ストフラ（A2345）
        makeHand(['S5', 'S2', 'S4', 'S6', 'S3']),   # ストフラ（23456）
        makeHand(['DT', 'D8', 'D9', 'DJ', 'D7']),   # ストフラ（それ以外）
        makeHand(['D4', 'S4', 'C4', 'H4', 'H3']),   # フォーカード
        makeHand(['C6', 'S2', 'S6', 'H2', 'D2']),   # フルハウス（ハイ2枚-ロー3枚）
        makeHand(['HQ', 'SQ', 'DQ', 'D3', 'S3']),   # フルハウス（ハイ3枚-ロー2枚）
        makeHand(['S4', 'SK', 'S2', 'SJ', 'S8']),   # フラッシュ
        makeHand(['ST', 'SK', 'CQ', 'CJ', 'SA']),   # ストレート（AKQJT）
        makeHand(['D3', 'HA', 'S4', 'H2', 'C5']),   # ストレート（A2345）
        makeHand(['C5', 'S2', 'S4', 'S6', 'S3']),   # ストレート（23456）
        makeHand(['DT', 'D8', 'D9', 'DJ', 'C7']),   # ストレート（それ以外）
        makeHand(['C6', 'S6', 'S5', 'H2', 'D6']),   # スリーカード（キッカーより高い）
        makeHand(['C6', 'S2', 'S5', 'H2', 'D2']),   # スリーカード（キッカーより低い）
        makeHand(['HQ', 'SQ', 'DJ', 'D3', 'SJ']),   # ツーペア
        makeHand(['CA', 'D3', 'DK', 'SA', 'S4']),   # ワンペア
        makeHand(['DJ', 'S6', 'CT', 'H5', 'D8'])    # ハイカード
    ]

    # ハンドの役を判定する
    print('----------')
    for hand in testcases:
        print(f'{", ".join([str(card) for card in hand])} - {getHandName(hand).value}')
    print('----------')