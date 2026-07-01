from boardgame.proc import Proc
from boardgame.table import Table
from boardgame.event_type import EventType as ev
from boardgame.dto import OutputEvent

class ProcGameStart(Proc):
    '''ゲーム開始処理。個々のゲームに応じてオーバーライドする。'''
    def do(self, table:Table) -> OutputEvent:
        return self.createEvent(table)

    def createEvent(self, table:Table) -> OutputEvent:
        '''ゲーム卓の出力用DTOを作成して返す。'''
        event = OutputEvent(event_type=ev.START_GAME)
        return event

if __name__ == '__main__':
    pass