from abc import abstractmethod

from boardgame.rules import Rules
from boardgame.player import Player
from boardgame.table import Table
from boardgame.dto import InputData, OutputEvent
from boardgame.event_type import EventType as ev

from boardgame.proc import Proc
from boardgame.proc_game_start import ProcGameStart
from boardgame.proc_game_end import ProcGameEnd

class Game:
    '''ゲーム論理手順。各手順を実行し、表示に必要な辞書データを返す。
    個々のゲームに応じて、defineProc()、setProc()、isGameEnd()、または他を上書きする。
    defineProc()を上書きする代わりに、self.procdicに値を追加してもよい。'''

    def __init__(self, input_data:InputData, rules:Rules, players:list[Player], pieces:list):
        '''ゲーム卓を作成し、プロシージャ定義を行う。
        Args:
            input_data (InputData): 処理用の入力データ。
            rules (Rules): ゲームのルール定義。
            players (list): プレイヤーのリスト。
            pieces (list): ゲームコンポーネントのリスト。
        '''
        self.input_data = input_data
        self.table = Table(rules=rules, players=players, pieces=pieces,
                           input_data=input_data, event=OutputEvent(event_type=ev.START_GAME))
        self.defineProc()

    def defineProc(self):
        '''プロシージャ定義。処理をオーバーライドしたら、ここの定義を上書きする。'''
        self.procdic: dict[str, Proc] = {
            'game_start' : ProcGameStart(),
            'game_end' : ProcGameEnd()
        }

    def start(self) -> OutputEvent:
        '''ゲームの開始処理。最初に実行したいものをProcGameStartのサブクラスに入れておいて、ここで実行する。
        Returns:
            OutputEvent: 表示用のイベントDTO。
        '''
        self.proc = self.procdic['game_start']
        self.event = self.proc.do(self.table)
        return self.event

    def next(self) -> OutputEvent:
        '''ゲームのメイン処理。ゲーム状態に応じたプロシージャを実行し、表示用イベントを返す。
        Returns:
            OutputEvent: 表示用のイベントDTO。
        '''
        self.proc = None
        self.setProc()
        if self.proc:
            self.event = self.proc.do(self.table)
            return self.event
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