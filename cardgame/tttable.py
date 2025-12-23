from playingcards.deck import Deck
from cardgame.table import Table
from cardgame.ttrules import TTRules

class TTTable(Table):
    '''トリックテイキングのゲーム卓。ゲームに必要なデータを保持する。'''
    def __init__(self, inputData:dict, rules:TTRules=TTRules(), deck:Deck=Deck().shuffle()):
        '''デフォルトのルールをトリックテイキング用ルールにする。'''
        super().__init__(inputData=inputData, rules=rules, deck=deck)

# 単体テスト
if __name__ == '__main__':
    from cardgame.playertype import PlayerType as Type
    inputData = {'player_types': [Type.HUMAN, Type.AI_RANDOM],
              'player_names': ['You', 'CPU']}
    table = Table(inputData=inputData)
    for elem in table.__dict__.items():
        print(elem)