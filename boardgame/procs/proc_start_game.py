from boardgame.procs.proc import Proc
from boardgame.event_type import EventType as ev
from boardgame.dto import OutputData
from boardgame.table import Table


class ProcStartGame(Proc):
    '''ゲーム開始処理。個々のゲームに応じてオーバーライドする。'''

    def do(self, table: Table) -> OutputData:
        return self.create_output_data(table)

    def create_output_data(self, table: Table) -> OutputData:
        '''ゲーム卓の出力用DTOを作成して返す。'''
        output_data = OutputData(event_type=ev.START_GAME)
        return output_data