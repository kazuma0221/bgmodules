from cardgame.proc import Proc
from cardgame.procdeal import ProcDeal

class ProcInitData(Proc):
    '''トリック開始時の出力データ初期化処理の実装。'''
    def do(self):
        '''現在は空メソッド'''
        pass

if __name__ == '__main__':
    # 卓セットアップ
    from cardgame.tttable import TTTable
    from cardgame import inputData

    table = TTTable(inputData=inputData.makeTestData())
    ProcDeal().do(table)
    ProcInitData().do()
    for item in table.event.items():
        print(item)