from dataclasses import dataclass
from boardgame.event_type import EventType

@dataclass(frozen=True)
class InputData:
    '''PR層からAP層へ、ゲーム入力を引き渡すためのデータ転送オブジェクト(DTO)の基底クラス。
    継承時の引数順序エラー（TypeError）を防ぐため、デフォルト値のあるフィールドは定義しない。
    '''
    pass

@dataclass(frozen=True)
class OutputEvent:
    '''AP層からPR層へ、ゲーム状態の変更を通知するためのデータ転送オブジェクト(DTO)の基底クラス。
    継承時の引数順序エラー（TypeError）を防ぐため、デフォルト値のあるフィールドは定義しない。
    '''
    event_type: EventType