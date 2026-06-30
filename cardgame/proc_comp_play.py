from cardgame.proc import Proc
from cardgame.table import Table
from cardgame.event_type import EventType as ev

class ProcCompPlay(Proc):
    '''コンピュータプレイ処理の実装。'''
    def do(self, table:Table):
        '''手札から1枚プレイする。'''
        cpu = table.players[table.turn]
        card = cpu.playCard(cpu.chooseCard(table))
        table.playedCards.append(card[1])

        # イベント設定
        table.event['MY_CHOICE'] = card[0]
        table.event['TURN_PLAYER'] = table.turn
        table.event['PLAYED_CARDS'] = table.playedCards
        table.event['EVENT_TYPE'] = ev.OPPONENT_TURN

# テスト
if __name__ == '__main__':
    from cardgame.input_data import InputData
    from cardgame.player_type import PlayerType as T
    from cardgame.trick_taking_rules import TrickTakingRules

    # 入力データとゲームテーブルを作成
    input_data = InputData(names=['A', 'B', 'C', 'D'],
                           types=[T.AI_RANDOM, T.AI_RANDOM, T.AI_RANDOM, T.AI_RANDOM])
    table = Table(input_data, rules=TrickTakingRules())
    
    # ディール
    from cardgame.proc_deal import ProcDeal
    proc = ProcDeal()
    proc.do(table)
    
    # データ初期化処理
    from cardgame.proc_trick_init import ProcTrickInit
    proc = ProcTrickInit()
    proc.do(table)
    
    # 検証：CPUプレイ前後の手札を表示
    player = table.players[table.turn]
    print(', '.join([card.string() for card in player.getHand()]))
    print('---')
    proc = ProcCompPlay()
    proc.do(table)
    print(table.playedCards[-1].string())
    print('---')
    print(', '.join([card.string() for card in player.getHand()]))