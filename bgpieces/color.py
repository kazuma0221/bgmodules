from enum import Enum

class Color(str, Enum):
    '''ゲーム内の色を表す、strをmixinした列挙型。コンポーネントやプレイヤーの色に使う。'''
    WHITE = 'WHITE'
    BLACK = 'BLACK'
    BLUE = 'BLUE'
    YELLOW = 'YELLOW'
    RED = 'RED'
    GREEN = 'GREEN'
    PINK = 'PINK'
    PURPLE = 'PURPLE'
    SKYBLUE = 'SKYBLUE'

    def names():
        '''列挙名の一覧を文字列のイテラブルで返す。'''
        return Color.__members__

    def items():
        '''列挙したEnum値の一覧をイテラブルで返す。'''
        return Color._member_map_.values()

    def values():
        '''列挙したEnum値の、実際の値の一覧をリストで返す。'''
        return [c.value for c in Color._member_map_.values()]

# テスト
if __name__ == '__main__':
    # Enumオブジェクトの文字列表現と、オブジェクト自体のペアを列挙
    # タプルの左側は実際の値ではなく、左辺の変数名がstrになって返されている
    print(Color.BLACK.casefold())
    for c in Color._member_map_.items():
        print(c)
    # 文字列表現のみ
    for c in Color.names():
        print(c)
    # Enumオブジェクトのみ
    for c in Color.items():
        print(c)
    # 値のみ
    for c in Color.values():
        print(c)