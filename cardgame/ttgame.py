from cardgame.tttable import TTTable
from cardgame.playertype import PlayerType

from cardgame.proc import Proc
from cardgame.procdeal import ProcDeal
from cardgame.proctrickinit import ProcTrickInit
from cardgame.prochumanplay import ProcHumanPlay
from cardgame.proccompplay import ProcCompPlay
from cardgame.proctrickresult import ProcTrickResult
from cardgame.procdealresult import ProcDealResult

class TTGame():
    '''トリックテイキングのゲーム論理手順。各手順を実行し、表示に必要な辞書データを返す。'''
    def __init__(self, inputData:dict):
        '''ゲーム卓を作成し、プロシージャ定義を行う。
        :param dict inputData: AP層用の入力データ。'''
        self.table = TTTable(inputData=inputData)
        self.defineProc()

    def defineProc(self):
        '''プロシージャ定義。処理をオーバーライドしたら、ここの定義を上書きする。'''
        self.procdic: dict[str, Proc] = {
            'deal' : ProcDeal(),
            'trickinit' : ProcTrickInit(),
            'trickresult' : ProcTrickResult(),
            'humanplay' : ProcHumanPlay(),
            'compplay' : ProcCompPlay(),
            'dealresult' : ProcDealResult()
        }

    def start(self):
        '''ディールの開始処理。'''
        self.proc = self.procdic['deal']
        self.proc.do(self.table)
        return self.table.event

    def isDealEnd(self):
        '''ディールの終了判定処理。場札も全員の手札もなくなったらディール終了。
        終了ならTrue、まだならFalseを返す。'''
        return (len(self.table.playedCards) == 0) \
                and sum([len(player.getHand()) for player in self.table.players]) < 1

    def next(self, inputData):
        '''ゲームのメイン処理。表示用イベントを返す。'''
        # 入力と初期値
        self.table.inputData = inputData
        self.proc = None
        cardCnt = len(self.table.playedCards)

        # プロシージャを設定
        self.setProc(cardCnt)

        # 対応するプロシージャを実行し、イベントを返す
        if self.proc is not None:
            self.proc.do(self.table)
        # カードが出ていれば、手番を次に進める
        if len(self.table.playedCards) > cardCnt:
            self.table.turn = (self.table.turn + 1) % len(self.table.players)
        # イベントを返す
        return self.table.event

    def setProc(self, cardCnt):
        '''ゲーム状態に応じて実行すべきプロシージャオブジェクトを設定する。'''
        # ディールが終了したら終了処理
        if self.isDealEnd():
            self.proc = self.procdic['dealresult']
        # クリアフラグがオンなら、トリックのリセット（次トリックの開始処理）
        elif self.table.inputData['clear']:
            self.table.inputData['clear'] = False
            self.proc = self.procdic['trickinit']
        # トリック未解決で全員が出したら、トリック解決
        elif cardCnt >= len(self.table.players):
            self.proc = self.procdic['trickresult']
        # トリックの途中なら、プレイヤーの手番
        else:
            if self.table.players[self.table.turn].getType() == PlayerType.HUMAN:
                self.proc = self.procdic['humanplay']
            else:
                self.proc = self.procdic['compplay']