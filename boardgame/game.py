from abc import abstractmethod

from boardgame.dto import InputData, OutputData
from boardgame.proc import Proc
from boardgame.proc_game_start import ProcGameStart
from boardgame.proc_game_end import ProcGameEnd

class Game:
    '''ゲーム論理手順。各手順を実行し、表示に必要な出力DTOを返す。
    個々のゲームに応じて、defineProc()、setProc()、isGameEnd()、または他を上書きする。
    defineProc()を上書きする代わりに、self.procdicに値を追加してもよい。'''

    def __init__(self, input_data: InputData):
        '''ゲーム卓を作成し、プロシージャ定義を行う。
        Args:
            input_data (InputData): 処理用の入力データ。
        '''
        self.input_data = input_data
        self.defineProc()

    def defineProc(self):
        '''プロシージャ定義。処理をオーバーライドしたら、ここの定義を上書きする。'''
        self.procdic: dict[str, Proc] = {
            'game_start' : ProcGameStart(),
            'game_end' : ProcGameEnd()
        }

    def start(self) -> OutputData:
        '''ゲームの開始処理。最初に実行したいものをProcGameStartのサブクラスに入れておいて、ここで実行する。
        Returns:
            OutputData: 表示用の出力DTO。
        '''
        self.proc = self.procdic['game_start']
        self.output_data = self.proc.do(self.table)
        return self.output_data

    def next(self) -> OutputData:
        '''ゲームのメイン処理。ゲーム状態に応じたプロシージャを実行し、表示用イベントを返す。
        Returns:
            OutputData: 表示用の出力DTO。
        '''
        self.proc = None
        self.setProc()
        if self.proc:
            self.output_data = self.proc.do(self.table)
            return self.output_data
        return None

    def setProc(self):
        '''ゲームの流れ（ラウンド、フェーズ等）の実装。ゲーム状態に応じて実行すべきプロシージャオブジェクトを設定する。
        個々のゲームに合わせて、このメソッドを上書きする。'''
        # ゲーム終了処理を最初に判定する
        if self.isGameEnd():
            self.proc = self.procdic['game_end']
        # 以降はゲームに合わせて上書き実装する
        pass

    @abstractmethod
    def isGameEnd(self) -> bool:
        '''ゲームの終了判定処理。終了ならTrue、まだならFalseを返す。必ず上書きする。'''
        raise NotImplementedError