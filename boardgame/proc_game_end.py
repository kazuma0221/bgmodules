from boardgame.proc import Proc
from boardgame.table import Table
from boardgame.event_type import EventType as ev
from boardgame.dto import OutputData

class ProcGameEnd(Proc):
    '''ゲーム終了処理。個々のゲームに応じてオーバーライドする。'''
    def do(self, table: Table) -> OutputData:
        output_data = OutputData(event_type=ev.GAME_RESULT)
        return output_data

if __name__ == '__main__':
    pass