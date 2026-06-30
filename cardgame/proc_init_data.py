from cardgame.proc import Proc
from cardgame.proc_deal import ProcDeal

class ProcInitData(Proc):
    '''トリック開始時の出力データ初期化処理の実装。'''
    def do(self):
        '''現在は空メソッド'''
        pass

if __name__ == '__main__':
    # 卓セットアップ
    from cardgame.trick_taking_table import TrickTakingTable
    from cardgame import input_data

    table = TrickTakingTable(inputData=input_data.makeTestData())
    ProcDeal().do(table)
    ProcInitData().do()
    for item in table.event.items():
        print(item)