from enum import IntEnum

class Suit(IntEnum):
    '''トランプのスートを表す整数列挙型。ブリッジオーダー。'''
    X = 5   #ジョーカー
    Spades = 4
    Hearts = 3
    Diamonds = 1
    Clubs = 2

    def getMark(self):
        suits = {Suit.Spades:u'♠', Suit.Hearts:u'♡', Suit.Diamonds:u'♢', Suit.Clubs:u'♣', Suit.X:u'J'}
        return suits[self]

if __name__ == '__main__':
    print(Suit.Hearts.getMark())
    print(Suit.Spades.name[0:1].lower())
    print(Suit.Diamonds.value)