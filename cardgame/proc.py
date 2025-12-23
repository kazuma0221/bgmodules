from abc import ABC, abstractmethod

class Proc(ABC):
    '''カードゲームの手順を定義する親クラス。このクラスをStateパターンで継承して各処理を記述する。'''

    @abstractmethod
    def do(self):
        '''処理の実装。'''
        pass