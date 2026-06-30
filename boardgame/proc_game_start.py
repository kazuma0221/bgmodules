from boardgame.proc import Proc
from boardgame.table import Table
from boardgame.eventtype import EventType as ev

class ProcStartGame(Proc):
    '''ゲーム開始処理。個々のゲームに応じてオーバーライドする。'''
    def do(self, table:Table)->dict:
        # 初期値設定
        self.setEvent(table)
        return table.event

    def setEvent(self, table:Table):
        '''ゲーム卓の出力用辞書eventを作成する。'''
        table.event = {}
        table.event['EVENT_TYPE'] = ev.START_GAME
        # table.event['VALUE'] = somevalue のように書く

if __name__ == '__main__':
    pass