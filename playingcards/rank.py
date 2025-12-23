from enum import IntEnum

class Rank(IntEnum):
    '''トランプのランクを表す整数列挙型。Aが14、数字は数字通り、JQKは11,12,13。'''
    Ace = 14
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

    # 自分の名前を正式の（長い）文字列で返す
    def getFullName(self):
        return str(self).split('.')[-1]
    
    # 自分の名前を頭文字で返す
    def getName(self):
        if self.value == 0:
            return str(self).split('.')[-1]
        elif self.value < 11:
            return str(self.value)
        else:
            return str(self).split('.')[-1][0]

if __name__ == '__main__':
    import random
    r = Rank(random.randint(min(Rank).value, max(Rank).value))
    print('----------')
    print('Name: ' + str(r))
    print('Value: ' + str(r.value))
    print('getFullName(): ' + r.getFullName())
    print('getName(): ' + r.getName())
    print('----------')