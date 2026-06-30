from playingcards.deck import Deck
from cardgame.table import Table
from cardgame.trick_taking_rules import TrickTakingRules

class TrickTakingTable(Table):
    '''トリックテイキングのゲーム卓。ゲームに必要なデータを保持する。'''
    def __init__(self, inputData:dict, rules:TrickTakingRules=TrickTakingRules(), deck:Deck=Deck().shuffle()):
        '''デフォルトのルールをトリックテイキング用ルールにする。'''
        super().__init__(inputData=inputData, rules=rules, deck=deck)

# 単体テスト
if __name__ == '__main__':
    from cardgame.player_type import PlayerType as Type
    inputData = {'player_types': [Type.HUMAN, Type.AI_RANDOM],
              'player_names': ['You', 'CPU']}
    table = Table(inputData=inputData)
    for elem in table.__dict__.items():
        print(elem)