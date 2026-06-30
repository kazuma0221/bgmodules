from enum import Enum

class EventType(Enum):
    '''カードゲームのイベント種類を表す列挙型。文字列によって状態を表す。'''
    BEGIN_DEAL = 'BEGIN_DEAL'
    BEGIN_TRICK = 'BEGIN_TRICK'
    USER_TURN = 'USER_TURN'
    USER_APPROVED = 'USER_APPROVED'
    OPPONENT_TURN = 'OPPONENT_TURN'
    RESOLVE_TRICK = 'RESOLVE_TRICK'
    DEAL_RESULT = 'DEAL_RESULT'