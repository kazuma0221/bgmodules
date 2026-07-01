from abc import ABC, abstractmethod
from boardgame.table import Table
from boardgame.dto import OutputEvent

class Proc(ABC):
    '''ボードゲームの手順を定義する親クラス。このクラスをStateパターンで継承して各処理を記述する。'''
    @abstractmethod
    def do(self, table:Table) -> OutputEvent:
        '''処理の実装。出力用の辞書を必ず返す。
        Args:
            table (Table): データを保持するゲーム卓。
        Returns:
            OutputEvent: PR層に出力するためのDTO。'''
        raise NotImplementedError