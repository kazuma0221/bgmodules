import numpy as np
from bgpieces.piece import Piece
from bgpieces.color import Color

class Die(Piece):
    '''ダイスのクラス。値、面数、色を持つ。デフォルトでは1～6の6面ダイスになる。'''
    def __init__(self, value:int=1, sides:int=6, color:Color=Color.WHITE):
        '''初期値を設定し、乱数生成器を初期化する。
        :param int value: ダイスの示す値。
        :param int sides: ダイスの面数。
        :param Color color: ダイスの色。ゲームに使わなければデフォルトのままでよい。'''
        super().__init__(color=color, value=value, name='die')
        self.sides = sides
        self.rng = np.random.default_rng()

    def roll(self)->int:
        '''ダイスを振り、値を「1～面数のあいだの整数」でランダムに更新して返す。'''
        self.value = self.rng.choice(self.sides) + 1
        return self.value

    def flip(self)->int:
        '''ダイスを裏返す。6面ダイスの場合のみ裏返して値を返し、それ以外のダイスではNoneを返す。'''
        if self.sides == 6:
            self.value = 7 - self.value
            return self.value
        else:
            return None

# テスト
if __name__ == '__main__':
    die = Die()
    print(f'ROLL: {die.roll()}')
    print(f'FLIP: {die.flip()}')