from cardgame.proc import Proc
from cardgame.trick_taking_table import TrickTakingTable
from cardgame.event_type import EventType as ev

class ProcTrickInit(Proc):
    '''トリックテイキングの、各トリック開始時の出力データ初期化処理。'''
    def do(self, table:TrickTakingTable):
        '''テーブルのプレイカードと表示用のeventをトリック前の状態にする。'''
        del table.playedCards[:]
        table.event['EVENT_TYPE'] = ev.BEGIN_TRICK
        table.event['IS_PLAYABLE'] = True
        table.event['MY_CHOICE'] = -1
        table.event['HANDS'] = [p.getHand() for p in table.players]
        table.event['TURN_PLAYER'] = table.turn
        table.event['PLAYED_CARDS'] = table.playedCards
        table.event['TRICK_WINNER'] = -1

if __name__ == '__main__':
    from cardgame.proc_deal import ProcDeal
    from cardgame.input_data import makeTestData

    # ディールとトリック前処理を行い、データを確認
    table = TrickTakingTable(makeTestData())
    ProcDeal().do(table)
    ProcTrickInit().do(table)
    for item in table.event.items():
        print(item)