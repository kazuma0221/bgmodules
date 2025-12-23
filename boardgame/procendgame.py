from boardgame.proc import Proc
from boardgame.table import Table
from boardgame.eventtype import EventType as ev

class ProcEndGame(Proc):
    '''ゲーム終了処理。個々のゲームに応じてオーバーライドする。'''
    def do(self, table:Table)->dict:
        table.event['EVENT_TYPE'] = ev.GAME_RESULT
        return table.event

if __name__ == '__main__':
    pass