from cardgame.proc import Proc
from cardgame.table import Table
from cardgame.event_type import EventType as ev

class ProcDealResult(Proc):
    '''ディール結果判定の実装。'''
    def do(self, table:Table):
        self.scoring(table)
        table.output_data['EVENT_TYPE'] = ev.DEAL_RESULT

    def scoring(self, table:Table):
        '''得点計算。デフォルトでは、勝利数（トリック数など）を直接加算する。
        何らかの処理を行う場合、このメソッドを上書きする。'''
        # TODO: SCORESとTOTAL_SCORESの区別がよくわからないので、コードを見直す
        # 合計点の数字がおかしい
        for i, wins in enumerate(table.output_data['WIN_COUNTS']):
            table.scores[i] += wins
        for totalScore, score in zip(table.totalScores, table.scores):
            totalScore.append(score)
        table.output_data['SCORES'] = table.scores
        table.output_data['TOTAL_SCORES'] = table.totalScores