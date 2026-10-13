from boardgame.procs.proc import Proc
from boardgame.event_type import EventType as ev
from boardgame.dto import OutputData
from boardgame.table import Table


class ProcEndGame(Proc):
    '''ゲーム終了処理。個々のゲームに応じてオーバーライドする。'''

    def do(self, table: Table) -> OutputData:
        output_data = OutputData(event_type=ev.GAME_RESULT)
        return output_data