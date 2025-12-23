from enum import Enum

class EventType(Enum):
    '''ボードゲームのイベント種類を表す列挙型。文字列によって状態を表す。'''
    START_GAME = 'START_GAME'
    START_ROUND = 'START_ROUND'
    USER_TURN = 'USER_TURN'
    USER_APPROVED = 'USER_APPROVED'
    OPPONENT_TURN = 'OPPONENT_TURN'
    AUTO_MOVE = 'AUTO_MOVE'
    END_ROUND = 'END_ROUND'
    GAME_RESULT = 'GAME_RESULT'