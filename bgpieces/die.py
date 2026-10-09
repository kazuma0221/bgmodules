import numpy as np
from bgpieces.piece import Piece
from bgpieces.color import Color

class Die(Piece):
    '''ダイスのクラス。値、面数、色を持つ。デフォルトでは1～6の6面ダイスになる。'''

    def __init__(self, value: int = 1, sides: int = 6, color: Color = Color.WHITE):
        '''初期値を設定し、乱数生成器を初期化する。

        Args:
            value (int): ダイスの示す値。
            sides (int): ダイスの面数。
            color (Color): ダイスの色。ゲームに使わなければデフォルトのままでよい。
        '''
        super().__init__(color=color, value=value, name='die')
        self.sides = sides
        self.rng = np.random.default_rng()

    def roll(self) -> int:
        '''ダイスを振り、値を返す。

        Returns:
            int: 「1～面数」から選ばれたランダムな整数。
        '''
        self.value = self.rng.choice(self.sides) + 1
        return self.value

    def flip(self) -> int | None:
        '''ダイスを裏返し、値を返す。裏面の値は (面数 + 1 - 現在の面) で求める。

        Returns:
            int | None: 偶数面で6面以上のダイスでは裏返して値を返す。それ以外のダイスでは面を操作せずNoneを返す。
        '''
        if self.sides >= 6 and self.sides % 2 == 0:
            self.value = (self.sides + 1) - self.value
            return self.value
        else:
            return None


# テスト
if __name__ == '__main__':
    die = Die()
    print(f'ROLL: {die.roll()}')
    print(f'FLIP: {die.flip()}')