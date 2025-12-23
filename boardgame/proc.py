from abc import ABC, abstractmethod
from table import Table

class Proc(ABC):
    '''ボードゲームの手順を定義する親クラス。このクラスをStateパターンで継承して各処理を記述する。'''
    @abstractmethod
    def do(self, table:Table)->dict:
        '''処理の実装。出力用の辞書を必ず返す。'''
        pass