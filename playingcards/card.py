from functools import total_ordering

@total_ordering
class Card():
    '''カードゲームのカードを表すクラス。
    ランクとスートを設定して生成し、並べ替えや強さの比較が可能。
    大小比較は、スートの強さを比べ、同じならランクの強さを比べる。
    ランクとスートの型指定はなく、ダックタイピングに基づく独自実装でもよい。'''
    
    def __init__(self, rank, suit):
        '''ランクとスートをセットする。'''
        self.rank = rank
        self.suit = suit
    
    # 文字列表現（解析用としてスートは文字出力）
    def __str__(self):
        return str(self.suit.name).split('.')[-1] + '.' + str(self.rank.value)
    def __repr__(self):
        return str(self.suit.name).split('.')[-1] + '.' + str(self.rank.value)

    # ソート比較用
    def __eq__(self, obj):
        return (self.suit.value == obj.suit.value) and (self.rank.value == obj.rank.value)
    def __lt__(self, obj):
        if self.suit.value < obj.suit.value:
            return True
        elif self.suit.value > obj.suit.value:
            return False
        else:
            return self.rank.value < obj.rank.value

    # ゲッターとセッター
    def setRank(self, rank):
        self.rank = rank

    def getRank(self):
        return self.rank

    def setSuit(self, suit):
        self.suit = suit

    def getSuit(self):
        return self.suit

    def setPhoto(self, photo):
        self.photo = photo

    def getPhoto(self):
        return self.photo

    def string(self):
        return (self.suit.getMark() + self.rank.getName())

    def short(self):
        return (self.suit.name[0] + self.rank.getName())