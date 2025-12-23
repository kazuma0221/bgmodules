from bgpieces.color import Color

class Piece():
    '''ボードゲームのコマを表すクラス。
    大きさは問わない。色、値、名前（種類）を任意で持ってもよい。値、名前（種類）はどの型でもよい。'''
    def __init__(self, color:Color=None, value=None, name=None):
        '''色、値、名前（種類）をセットする。'''
        self.color:Color = color
        self.value = value
        self.name = name