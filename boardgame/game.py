from abc import abstractmethod

from boardgame.rules import Rules
from boardgame.player import Player
from boardgame.table import Table

from boardgame.proc import Proc
from boardgame.procstartgame import ProcStartGame
from boardgame.procendgame import ProcEndGame

class Game():
    '''ゲーム論理手順。各手順を実行し、表示に必要な辞書データを返す。
    個々のゲームに応じて、defineProc()、setProc()、isGameEnd()、または他を上書きする。
    defineProc()を上書きする代わりに、self.procdicに値を追加してもよい。'''

    def __init__(self, inputData:dict, rules:Rules, players:list[Player], pieces:list):
        '''ゲーム卓を作成し、プロシージャ定義を行う。
        :param dict inputData: 処理用の入力データ。'''
        self.inputData = inputData
        self.table = Table(rules=rules, players=players, pieces=pieces)
        self.defineProc()

    def defineProc(self):
        '''プロシージャ定義。処理をオーバーライドしたら、ここの定義を上書きする。'''
        self.procdic: dict[str, Proc] = {
            'startgame' : ProcStartGame(),
            'endgame' : ProcEndGame()
        }

    def start(self):
        '''ゲームの開始処理。最初に実行したいものをProcStartGameのサブクラスに入れておいて、ここで実行する。'''
        self.proc = self.procdic['startgame']
        return self.proc.do(self.table)

    def next(self)->dict:
        '''ゲームのメイン処理。ゲーム状態に応じたプロシージャを実行し、表示用イベントを返す。'''
        self.proc = None
        self.setProc()
        if self.proc is not None:
            return self.proc.do(self.table)
        return None

    def setProc(self):
        '''ゲームの流れ（ラウンド、フェーズ等）の実装。ゲーム状態に応じて実行すべきプロシージャオブジェクトを設定する。
        個々のゲームに合わせて、このメソッドを上書きする。'''
        # ゲーム終了処理を最初に判定する
        if self.isGameEnd():
            self.proc = self.procdic['endgame']
        # 以降はゲームに合わせて上書き実装する
        pass

    @abstractmethod
    def isGameEnd(self)->bool:
        '''ゲームの終了判定処理。終了ならTrue、まだならFalseを返す。必ず上書きする。'''
        pass