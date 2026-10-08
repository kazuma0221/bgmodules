from abc import ABC, abstractmethod


class BaseTurnPostProcessor(ABC):
    '''手番終了時の後処理を行う抽象基底クラス。'''

    @abstractmethod
    def process(self, table: object):
        '''手番終了時の後処理を実行する。

        Args:
            table: 現在のゲーム卓（DTO）。
        '''
        pass