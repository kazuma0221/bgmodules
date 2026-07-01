import numpy as np
import copy
from enum import IntEnum

DEFAULT_NAMES = [
    'Abigail',
    'Benjamin',
    'Chloe',
    'David',
    'Esme',
    'Frederica',
    'George',
    'Harper',
    'Isaac',
    'Jessica',
    'Kai',
    'Lottie',
    'Muhammad',
    'Naomi',
    'Owen',
    'Quinn',
    'Phoebe',
    'Rachel',
    'Sean',
    'Tabitha',
    'Ulysses',
    'Vincent',
    'Willow',
    'Xavier',
    'Yvonne',
    'Zachary'
]

class PlayerType(IntEnum):
    '''プレイヤーの種類を表す整数列挙型。実装に応じて追加してゆく。'''
    HUMAN = 0
    AI_RANDOM = 1

class Player:
    '''ボードゲームのプレイヤーを表すクラス。
    ゲーム卓（Table）側でPlayerオブジェクトを作成するので、循環参照を避けるため
    このファイルにTableクラスをimportしないこと。'''
    def __init__(self, ptype:PlayerType=PlayerType.AI_RANDOM, pname:str=None):
        '''プレイヤーのタイプと名前をセットし、乱数を初期化する。'''
        self.ptype: PlayerType = ptype
        self.pname: str = pname
        self.rng = np.random.default_rng()
        if self.pname is None:
            self.pname = self.rng.choice(DEFAULT_NAMES)

    def chooseOne(self, choices):
        '''引数でイテラブルを渡すと、1つをランダムに選択して返す。'''
        return self.rng.choice(choices)

def makePlayers(types:list[PlayerType], names:list[str]) -> list[Player]:
    '''プレイヤータイプ、名前のリストからPlayerのリストを作る。
    引数のリストは長いほうの長さを採用し、不足分は適宜埋める。

    Args:
        types (list[PlayerType]): プレイヤータイプのリスト。不足分はランダムAIにする。
        names (list[str]): 名前のリスト。不足分は所定の名前からランダムに追加する。
    Returns:
        list[Player]: プレイヤーのリスト。'''

    # リストの長いほうの長さを取得する
    len_types, len_names = len(types), len(names)
    max_length = max(len_types, len_names)

    # 不足分を埋める
    types += [PlayerType.AI_RANDOM] * (max_length - len_types)
    if len_names < max_length:
        filler = copy.copy(DEFAULT_NAMES)
        rng = np.random.default_rng()
        rng.shuffle(filler)
        names += filler[:(max_length - len_names)]

    # プレイヤーを生成して返す
    return [Player(ptype, pname) for ptype, pname in zip(types, names)]

# テスト
if __name__ == '__main__':
    # 1人適当に作る
    player = Player(PlayerType.AI_RANDOM)
    print(f'PLAYER TYPE: {player.ptype.name}')
    print(f'PLAYER NAME: {player.pname}')

    # AIを5人ぐらい作る
    types = [PlayerType.AI_RANDOM] * 5
    players = makePlayers(types, [])
    for player in players:
        print(f'NAME: {player.pname}, TYPE: {player.ptype.name}')