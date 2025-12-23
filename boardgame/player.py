import numpy as np
from enum import IntEnum

class PlayerType(IntEnum):
    '''プレイヤーの種類を表す整数列挙型。実装に応じて追加してゆく。'''
    HUMAN = 0
    AI_RANDOM = 1

class Player():
    '''ボードゲームのプレイヤーを表すクラス。
    ゲーム卓（Table）側でPlayerオブジェクトを作成するので、循環参照を避けるため
    このファイルにTableクラスをimportしないこと。'''
    def __init__(self, ptype:PlayerType=PlayerType.AI_RANDOM, pname:str='Default'):
        '''プレイヤーのタイプと名前をセットし、乱数を初期化する。'''
        self.ptype: PlayerType = ptype
        self.pname: str = pname
        self.rng = np.random.default_rng()

    def chooseOne(self, choices):
        '''引数で渡されたイテラブルから1つを選択して返す。'''
        return self.rng.choice(choices)

def makePlayers(types:list[PlayerType], names:list[str]):
    '''プレイヤータイプ、名前、手札のリストからPlayerオブジェクトのリストを作って返すユーティリティ関数。
    引数で受け取ったリストをzip()で展開するので、各リストの長さは同じであるのが望ましい。
    :param list types: プレイヤータイプのリスト。
    :param list names: 名前のリスト。'''
    return [Player(ptype=ptype, pname=pname) for ptype, pname in zip(types, names)]

# テスト
if __name__ == '__main__':
    player = Player(PlayerType.AI_RANDOM)
    print(f'PLAYER TYPE: {player.ptype}')
    print(f'PLAYER NAME: {player.pname}')