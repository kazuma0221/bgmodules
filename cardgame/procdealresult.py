from cardgame.proc import Proc
from cardgame.table import Table
from cardgame.eventtype import EventType as ev

class ProcDealResult(Proc):
    '''ディール結果判定の実装。'''
    def do(self, table:Table):
        self.scoring(table)
        table.event['EVENT_TYPE'] = ev.DEAL_RESULT

    def scoring(self, table:Table):
        '''得点計算。デフォルトでは、勝利数（トリック数など）を直接加算する。
        何らかの処理を行う場合、このメソッドを上書きする。'''
        # TODO: SCORESとTOTAL_SCORESの区別がよくわからないので、コードを見直す
        # 合計点の数字がおかしい
        for i, wins in enumerate(table.event['WIN_COUNTS']):
            table.scores[i] += wins
        for totalScore, score in zip(table.totalScores, table.scores):
            totalScore.append(score)
        table.event['SCORES'] = table.scores
        table.event['TOTAL_SCORES'] = table.totalScores