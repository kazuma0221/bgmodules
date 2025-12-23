from cardgame.proc import Proc
from cardgame.tttable import TTTable
from cardgame.eventtype import EventType as ev

class ProcTrickResult(Proc):
    '''トリック結果判定の実装。'''
    def do(self, table:TTTable):
        '''トリック結果を判定し、勝者を記録して次のリードに指定する。'''
        table.turn = (table.rules.whoWins(table.playedCards) + table.turn) % len(table.players)
        table.players[table.turn].pointPile.extend(table.playedCards)
        table.event['PLAYED_CARDS'] = table.playedCards
        table.event['TRICK_WINNER'] = table.turn
        table.event['WIN_COUNTS'][table.turn] += 1
        table.event['EVENT_TYPE'] = ev.RESOLVE_TRICK

if __name__ == '__main__':
    from cardgame import inputData
    from cardgame.playertype import PlayerType
    from cardgame.procdeal import ProcDeal
    from cardgame.proctrickinit import ProcTrickInit
    from cardgame.proccompplay import ProcCompPlay

    # 入力データとゲームテーブルを作成
    data = inputData.inputData
    inputData.setNames(['A', 'B', 'C', 'D'])
    inputData.setTypes([PlayerType.AI_RANDOM, PlayerType.AI_RANDOM, PlayerType.AI_RANDOM, PlayerType.AI_RANDOM])
    table = TTTable(inputData=data)
    
    # ディール、トリック開始
    ProcDeal().do(table)
    ProcTrickInit().do(table)

    # 切札と打ち出し
    table.rules.setTrump(table.players[table.dealer].getCard(-1))
    print('------------------SAMPLE TRICK------------------')
    print('Trump: ' + table.rules.getTrump().string() + ', Lead: ' + table.players[table.turn].pname)
    # 検証：4人でランダムプレイして、勝ちを決める
    print('---')
    proc = ProcCompPlay()
    for _ in range(len(table.players)):
        proc.do(table)
        print(table.players[table.turn].pname + ':' + table.playedCards[-1].string())
        table.turn = (table.turn + 1) % len(table.players)
    ProcTrickResult().do(table)
    print(f'The winner is {table.players[table.turn].pname}.')
    print('---')