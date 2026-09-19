from bgpieces.color import Color
from bgpieces.piece import Piece


class Card(Piece):
    '''汎用的なカードを表すクラス。

    Pieceを継承し、カードの表裏状態や表面情報を保持する。
    '''

    def __init__(self, color: Color = None, value=None, name=None,
                 is_face_up: bool = True, is_tapped: bool = False):
        '''カードの初期状態を設定する。

        Args:
            color (Color): カードの色。
            value: カードの値。
            name: カードの名前。
            is_face_up (bool): 表向きかどうか。デフォルトは True。
            is_tapped (bool): タップ状態かどうか。デフォルトは False。
        '''
        super().__init__(color=color, value=value, name=name)
        self.is_face_up: bool = is_face_up
        self.is_tapped: bool = is_tapped

    def flip(self):
        '''カードの表裏を反転させる。'''
        self.is_face_up = not self.is_face_up

    def tap(self):
        '''カードのタップ状態を反転させる。'''
        self.is_tapped = not self.is_tapped