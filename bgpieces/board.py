class Board():
    '''ボードゲームのボードを表すクラス。
    大きさは問わない。物を配置するスペースは必須で、名前（種類）は任意で、それぞれ持つ。
    '''

    def __init__(self, spaces: dict, name: str = None):
        '''スペースの辞書と、名前（種類）をセットする。

        Args:
            spaces (dict): 物を配置するスペースの辞書。各スペースの型は任意で、デフォルトのコレクションでも独自クラスでもよい。
            name (str): ボードの名前。設定しなくてもよい。
        '''
        self.spaces: dict = spaces
        self.name: str = name